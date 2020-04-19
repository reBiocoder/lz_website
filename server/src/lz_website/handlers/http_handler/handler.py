from os.path import dirname, realpath, basename, join, exists
from plotnine import *
import pandas as pd
import numpy as np
import os
from mg_app_framework import (HttpBasicHandler, MesCode, get_context, get_logger,
                              )
from mg_app_framework.config import Store

from lz_website.config import ConfigStore
from lz_website.util import NCBI
from lz_website.util.query_util import (use_locustag_get_result,
                                        validate_user_info,
                                        register_user_info,
                                        create_padj_and_log2_collection,
                                        random_data, random_column,
                                        get_search_table, get_search_one,
                                        get_environment_result, get_all_keys,
                                        get_image_json)
from lz_website.auth.hashers import make_password, set_cookie, login_required
from lz_website.util.redis_util import (insert_data,
                                        get_data
                                        )
from lz_website.auth.hashers import (login_required)
import json
import uuid


def uuid_naming_strategy() -> str:
    "File naming strategy that ignores original name and returns an UUID"
    return str(uuid.uuid4())


def csv_insert_to_mongodb(colletion):
    pass


def get_file_upload_path():
    """得到csv文件上传路径"""
    work_dir = dirname(dirname(dirname(realpath(__file__))))
    upload_path = join(work_dir, 'media', 'csv', uuid_naming_strategy() + '.csv')
    return upload_path


def get_image_upload_path():
    """得到图片的保存路径"""
    work_dir = dirname(dirname(dirname(realpath(__file__))))
    upload_path = join(work_dir, 'media', 'image')
    return upload_path


class CustomBasicHandler(HttpBasicHandler):
    """
    :type自定义handler
    """

    def prepare(self):
        self.application.settings["cookie_secret"] = "12345"
        print(self.current_user)

    def get_current_user(self):
        user_cookie = self.get_secure_cookie("session_id")  # {"username": "周鹏"}
        if user_cookie:
            return json.loads(user_cookie)
        return None


class UploadFileHandler(CustomBasicHandler):
    async def options(self, *args, **kwargs):
        self.send_response_data(code=MesCode.success, data={}, info="成功")

    async def post_process(self, *args, **kwargs):
        """
        上传csv文件, 自动导入mongodb
        :param args:
        :param kwargs:
        :return:
        """
        get_logger().info("正在上传文件")
        if 'csv_data' not in self.request.files:
            self.send_response_data(MesCode.fail, info="params error")
        else:
            raw_file = self.request.files["csv_data"][0]
            raw_file_name = raw_file.filename
            col_name = self.request.arguments["table"][0].decode("utf-8")
            tail_name = raw_file_name.split('.')[-1]  # 文件后缀名
            if str(tail_name).lower() != 'csv':
                self.send_response_data(MesCode.fail, info="not support file name")
            else:  # 在这里处理csv文件
                try:
                    file_path = get_file_upload_path()
                    print(file_path)
                    with open(file_path, 'wb') as f:
                        f.write(raw_file.body)
                    get_logger().info("%s上传了%s, 保存的名称为%s",
                                      str(self.request.remote_ip), raw_file_name, basename(file_path)
                                      )
                    # 将文件导入Mongodb中
                    sys_path = file_path
                    command = "mongoimport  --db lz_database --collection " + col_name + " --type csv --headerline --ignoreBlanks --file " + sys_path
                    print(command)
                    sys_res = os.system(command)
                    if sys_res == 0:  # 系统调用成功
                        self.send_response_data(MesCode.success, info=" 数据插入成功")
                    else:
                        self.send_response_data(MesCode.fail, info=" 数据插入失败")
                except IOError as e:
                    get_logger().error(
                        "文件出现写入错误%s" % e
                    )
                    self.send_response_data(MesCode.fail, info="IOError")


class LoginHandler(CustomBasicHandler):
    async def post_process(self, *args, **kwargs):
        """
        登录模块
        :type
        """
        username = self.data.get('username', None)
        password = self.data.get('password', None)
        if username and password:
            validate_user_result = await validate_user_info(username)
            if validate_user_result is None:
                self.send_response_data(MesCode.login, info="该用户没有注册")
            else:  # 验证密码正确性
                real_name = validate_user_result["real_name"]
                if validate_user_result["password"] == make_password(password):
                    # set cookie
                    self.set_secure_cookie("session_id", set_cookie(username, real_name), expires_days=1, path='/')
                    self.send_response_data(MesCode.success, {"real_name": real_name, "username": username},
                                            info="身份验证成功")
                else:
                    self.send_response_data(MesCode.fail, {'res': 'password error'}, info="密码错误")
        else:
            self.send_response_data(MesCode.fail, info="信息输入有误")


class RegisterHandler(CustomBasicHandler):
    async def post_process(self, *args, **kwargs):
        """
        注册模块
        :param args:
        :param kwargs:
        :return:
        """
        raw_name = self.data.get('real_name', None)
        raw_username = self.data.get('username', None)
        raw_password = self.data.get('password', None)
        if raw_name is None or raw_username is None or raw_password is None:
            self.send_response_data(MesCode.fail, info="提交信息不全")
        else:
            result = await register_user_info(raw_name,
                                              raw_username,
                                              raw_password)
            if result:
                # 设置用户cookie
                self.set_secure_cookie("session_id", set_cookie(raw_username, raw_name), expires_days=1)
                self.send_response_data(MesCode.success, info="注册成功")
            else:
                self.send_response_data(MesCode.fail, info="用户信息已经存在")


class IndexHandler(CustomBasicHandler):
    """主页展示表格中的数据"""

    async def get_process(self, *args, **kwargs):
        data = await random_data('tss', 'utex')
        if type(data[0]) == bytes:
            get_logger().info("从redis中得到数据")
            res_data = [eval(i.decode("utf-8")) for i in data]
        else:
            get_logger().info("从mongo集合中得到数据")
            res_data = data
        self.send_response_data(MesCode.success, data=res_data, info="成功得到首页数据")


class IndexColHandler(CustomBasicHandler):
    """主页表格中的列名"""

    async def get_process(self, *args, **kwargs):
        data = await random_column('tss', 'utex')
        col = []
        for i in data:
            temp_dict = {"align": "center", "sortable": "true"}
            temp_dict.update({"name": i, "label": i, "field": i})
            col.append(temp_dict)
        self.send_response_data(MesCode.success, data=col, info="成功得到列数据")


class SearchTableHandler(CustomBasicHandler):
    async def post_process(self, *args, **kwargs):
        """模糊搜索得到匹配结果"""
        keywords = self.data["q"]
        result = await get_search_table('tss', 'utex', keywords)
        self.send_response_data(MesCode.success, result, info="成功得到搜索结果")


class SearchOneHandler(CustomBasicHandler):
    async def post_process(self, *args, **kwargs):
        """精确搜索结果,基本结果"""
        keywords = self.data["q"]
        result = await get_search_one('tss', 'utex', keywords)
        self.send_response_data(MesCode.success, result, info="得到精确搜索结果")


class SearchEnvironmentHandler(CustomBasicHandler):
    async def post_process(self, *args, **kwargs):
        """精确搜索, 环境结果"""
        keywords = self.data["q"]
        get_logger().info("搜索的内容为%s", keywords)
        result = await get_environment_result(keywords)
        self.send_response_data(MesCode.success, result, info="得到精确搜索结果,环境标签")


class EnvironmentImageHandler(CustomBasicHandler):
    async def post_process(self, *args, **kwargs):
        print(self.request.headers)
        """环境结果, 得到火山图"""
        from mg_app_framework.web import StaticFileBasicHandler
        keywords = self.data["q"]
        raw_result = await get_image_json(keywords)
        json_result = json.dumps(raw_result)
        # 判断静态文件夹中是否存在该图片
        file_path = join(get_image_upload_path(), str(keywords) + ".png")
        if exists(file_path):  # 如果该图片已经存在
            get_logger().info("图片已经存在")
        else:
            #  #################图片处理######################
            df = pd.read_json(json_result)
            img = ggplot(df, aes('log2', "-1*np.log10(padj)", color='factor(threshold)')) + \
                  theme(axis_line=element_line(color="black"), panel_background=element_rect(fill='white')) + \
                  geom_point() + \
                  geom_text(aes(label='condition'), hjust='right', vjust='bottom', size=10,
                            position=position_dodge(width=1)) + \
                  scale_color_manual(values=("red", "grey")) + \
                  geom_hline(aes(yintercept=2, ), color="gray", linetype='dotted') + \
                  geom_vline(aes(xintercept=-1), color="gray", linetype='dotted') + \
                  geom_vline(aes(xintercept=1), color="gray", linetype='dotted') + \
                  labs(title=keywords) + xlab("log2FoldChange") + ylab("-1*log10(padj)")
            img.save(keywords, path=get_image_upload_path())
            get_logger().info("%s:火山图保存成功", keywords)
        re_url = str(self.request.headers['Origin'])+ "/api/image/" + str(keywords) + ".png"
        print("url:",re_url)
        data = {
            "locus_tag": keywords,
            "img_url": re_url
        }
        self.send_response_data(MesCode.success, data=data, info="图片获取成功")


class PubmedHandler(CustomBasicHandler):
    async def post_process(self, *args, **kwargs):
        """请求pubmed接口id"""
        keywords = self.data["q"]
        try:
            print("尝试得到pubmed")
            ncbi = NCBI.BaseNcbi(keywords)
            print("成功得到pubmed结果")
            article_list = await ncbi.getRefArticleInfo()
            data = {"code": 0, "msg": "Get related literature", "count": len(article_list), "result": article_list}
            self.send_response_data(MesCode.success, data=data, info="得到数据成功")
        except Exception as e:
            get_logger().error("得到pubmed数据错误 %s" % e)
            self.send_response_data(MesCode.fail, {}, info="获取pubmed数据失败")


class ColKeyNameHandler(CustomBasicHandler):
    """得到一个集合的键名"""

    @login_required
    async def post_process(self, *args, **kwargs):
        col_name = self.data['col_name']  # 得到查询的集合名称
        res_list = await get_all_keys(col_name)
        return self.send_response_data(MesCode.success, {"col_keys": res_list}, info="得到数据成功")


class WebHandler(CustomBasicHandler):
    async def get_process(self):
        num_data = {}
        self.send_response_data(MesCode.success, num_data, 'success get data')

    async def post_process(self):
        num_data = {}
        self.send_response_data(MesCode.success, num_data, 'success post data')


class DefaultConfigHandler(CustomBasicHandler):
    async def get_process(self, *args, **kwargs):
        self.set_header('Content-Type', 'application/json; charset=UTF-8')
        print(Store.context)
        print(Store.store.data)
        print(ConfigStore.data)
        print("123456")
        b = dict()

        a = await use_locustag_get_result('M744_RS00015')
        print(type(a))
        self.send_response_data(MesCode.success, json.dumps(a), "成功数据")


if __name__ == '__main__':
    work_dir = dirname(dirname(dirname(realpath(__file__))))
    app = basename(dirname(realpath(__file__)))
    log_path = join(work_dir, 'media', app + '.csv')
    uuid_path = join(work_dir, '.appid')
    print(work_dir)
    print(app)
    print(log_path)
    print(uuid_path)
