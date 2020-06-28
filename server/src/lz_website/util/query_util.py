#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author ：biocoder
# Date   ：2020/3/28 0028 下午 20:44
# *********************************
from mg_app_framework import (get_handler, get_store,
                              TaskKey, get_logger)
from lz_website.auth.hashers import make_password

import re
import datetime


#  精确搜索api
async def use_locustag_get_result(locus_tag=None):
    mongo_client = get_handler(TaskKey.mongodb_async)
    db = mongo_client['lz_database']
    tss_col = db['tss']
    gen_exp_col = db["gen_exp"]
    utex_col = db['utex']
    # M744_RS00015
    utex_result = await utex_col.find_one({"Locus_tag": locus_tag})
    tss_result = await tss_col.find_one({"Locus_tags": locus_tag})
    gen_exp_result = await gen_exp_col.find_one({"Locus_tags": locus_tag})
    print("*****************%s" % utex_result)
    #  返回的结果模式
    tss = {}
    if tss_result:
        tss["locus_tags"] = tss_result['Locus_tags']
        tss["tss_no"] = tss_result["TSS_ID"]
        tss["chromosome"] = tss_result['Chromosome']
        tss["strand"] = tss_result['Strand']
        tss["position"] = tss_result['Position']
        tss["distances"] = tss_result['Distances to start codon']
    utex = {}
    if utex_result:
        utex["locus_tags"] = utex_result['Locus_tag']
        utex["chrs"] = utex_result['Chrs']
        utex["start"] = utex_result['Start']
        utex["end"] = utex_result['End']
        utex["strand"] = utex_result['Strand']
        utex["utex_id"] = utex_result['ID']
        utex["type"] = utex_result['Type']
        utex["old_locus_tags"] = utex_result['Old_locus_tag']
        utex["product"] = utex_result['Product']
        utex["proaccno"] = utex_result['ProAccNo']
    genexp = {}
    if gen_exp_result:
        genexp["locus_tags"] = gen_exp_result['Locus_tags']
        genexp["tss_no"] = gen_exp_result['TSS_ID']
        genexp["gene_synbols"] = gen_exp_result['Gene Symbols']
        genexp["Max_Norm_Reads"] = gen_exp_result['Max_Norm_Reads']
        genexp["DK_vs_CT_log2FoldChange"] = gen_exp_result['DK_vs_CT_log2FoldChange']
        genexp["DK_vs_CT_padj"] = gen_exp_result['DK_vs_CT_padj']
        genexp["HL_vs_CT_log2FoldChange"] = gen_exp_result["HL_vs_CT_log2FoldChange"]
        genexp["HL_vs_CT_padj"] = gen_exp_result['HL_vs_CT_padj']
        genexp["HT_vs_CT_log2FoldChange"] = gen_exp_result['HT_vs_CT_log2FoldChange']
        genexp["HT_vs_CT_padj"] = gen_exp_result['HT_vs_CT_padj']
        genexp["Product"] = gen_exp_result['Product']
    result = {
        "tss": tss,
        "utex": utex,
        "genexp": genexp
    }
    return result


# 查询用户信息
async def validate_user_info(username=None):
    """
    该集合存储用户的账号和密码，进行权限认证
    :param username: 用户名
    :return: 若mongo中没有该用户，则返回None，若存在该用户则返回用户的collection
    """
    mongo_client = get_handler(TaskKey.mongodb_async)
    lz_database_db = mongo_client["lz_database"]
    lz_database_collection = lz_database_db['user_information']
    search_user = await lz_database_collection.find_one({"username": username})
    return search_user


# 注册用户信息
async def register_user_info(name=None, username=None, password=None) -> bool:
    """
    :param name:  用户的姓名
    :param username: 用户的账号
    :param password: 用户的密码
    :return:如果用户的姓名存在或者用户的账号存在,则返回False,注册失败. 如果不存在,则返回True,注册成功
    """
    mongo_client = get_handler(TaskKey.mongodb_async)
    lz_db = mongo_client["lz_database"]
    lz_col = lz_db["user_information"]
    # 用户名是否被注册过
    search_user = await lz_col.find_one({"username": username})
    # 用户的姓名
    search_name = await lz_col.find_one({"real_name": name})
    if search_user or search_name:
        return False
    else:
        await lz_col.insert_one({"real_name": name, "username": username, "password": make_password(password)})
        return True


# 得到mongo中一个collection的所有键名
async def get_all_keys(raw_col=None) -> list:
    # mongo_client = get_handler(TaskKey.mongodb_async)
    # db = mongo_client["lz_database"]
    # raw_col = db[raw_col]
    mongo_client = get_handler(TaskKey.mongodb_async)
    lz_db = mongo_client["lz_database"]
    raw_col = lz_db[raw_col]
    keys_list = []
    async for i in raw_col.find({}).limit(1):
        for name in i.keys():
            keys_list.append(name)
    if '_id' in keys_list:
        keys_list.remove('_id')  # 删除_id
    return keys_list


# 得到所有含有padj和log2FoldChange的键名
def get_all_padj_and_log2FoldChange_keys(keys_list: list, identify: str, split: str = '_') -> dict:
    """
    :param keys_list: 最开始的所有的键列表
    :param identify:padj和logkey 的标识符
    :param split: 键名的分隔符
    :return: {"DK_vs_CT_log2FoldChange": "DK_vs_CT"}
    """
    result = {}
    for i in keys_list:
        if str(i).endswith(identify):
            b = i
            c = "_".join(b.split('_')[0:-1])
            result.update({i: c})
    return result


async def get_environment_result(locus_tag: str, raw_col: str = 'gen_exp') -> list:
    """这里用的标记是locus_tags"""
    # import motor
    # mongo_client = motor.MotorClient()
    mongo_client = get_handler(TaskKey.mongodb_async)
    db = mongo_client["lz_database"]
    col = db["padj_log2"]  # 得到padj_log2集合
    col_count = await col.estimated_document_count()  # 集合中文档的数量
    if col_count:  # 存在文档
        result = []
        async for i in col.find({"locus_tags": locus_tag}):
            del i["_id"]  # 删除主键
            result.append(i)
        return result
    else:  # 不存在该文档
        create_col = await create_padj_and_log2_collection(str(raw_col))
        return []


# 处理genexp表格中的数据,
async def create_padj_and_log2_collection(raw_col: str = None):
    """
    约定 db:lz_database
        padj_log2的存储集合为 padj_log2
    处理raw_collection中的key
    :param raw_col:
    :return:
    """
    raw_col_str = raw_col
    mongo_client = get_handler(TaskKey.mongodb_async)
    db = mongo_client["lz_database"]
    if raw_col_str:
        raw_col = db[raw_col_str]  # 得到初始的集合
        padj_and_log2_col = db["padj_log2"]  # 得到padj_log2集合
        raw_keys_name = await get_all_keys(raw_col_str)
        padj_dict = get_all_padj_and_log2FoldChange_keys(raw_keys_name, 'padj')
        log2_dict = get_all_padj_and_log2FoldChange_keys(raw_keys_name, 'log2FoldChange')
        # 遍历整张raw_col表格
        async for i in raw_col.find():
            for j in padj_dict.keys():
                padj_log2_result = {}
                padj_log2_result.update({
                    "padj": i.get(j, ''),
                    "condition": padj_dict[j],
                    "locus_tags": i.get('Locus_tags', '')
                })
                for k, v in log2_dict.items():
                    if v == padj_dict[j]:
                        padj_log2_result.update({
                            "log2": i.get(k, '')
                        })
                        #  log2与padj全部插入完成,处理其中的问题数据,默认为0
                        padj_log2_result["threshold"] = get_threshold(padj_log2_result['log2'],
                                                                      padj_log2_result['padj'])
                        break
                    # else:
                    #     padj_log2_result.update({"log2": 0, "threshold": False})
                await padj_and_log2_col.insert_one(padj_log2_result)
        return True
    else:
        return False


def get_threshold(log2, padj) -> bool:
    """计算threshold"""
    get_logger().info("log2的类型%s,padj的类型%s" % (type(log2), type(padj)))
    if isinstance(log2, float) and isinstance(padj, float):
        if log2 is not None:
            if log2 > 1 or log2 < -1:
                if padj is not None and padj < 0.01:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False  # 数据缺失


async def random_column(first_col: str, second_col: str) -> list:
    """得到首页显示中的列"""
    mongo_client = get_handler(TaskKey.mongodb_async)
    db = mongo_client["lz_database"]
    new_col = first_col + '_' + second_col  # 新增集合名称
    async for i in db[new_col].aggregate([{"$project": {"_id": 0}},
                                          {"$limit": 1}
                                          ]):
        random_col = [j for j in i.keys()]
    return random_col


async def random_data(first_col: str, second_col: str) -> list:
    """首页随机显示数据"""
    # import motor, aioredis
    # mongo_client = motor.MotorClient()
    # redis_client = await aioredis.create_redis(('127.0.0.1', '6379'))
    mongo_client = get_handler(TaskKey.mongodb_async)
    redis_client = get_handler(TaskKey.redis_async)
    conn = await redis_client.get_connection()
    if conn:
        query_key = first_col + '_' + second_col
        query_is_exist = await conn.exists(query_key)
        if query_is_exist:
            result = await conn.lrange(query_key, 0, 99)
            get_logger().info("主页数据存在redis缓存")
            return result  # 二进制
        else:
            result = await merge_two_collection(first_col, 'Locus_tags', second_col, 'Locus_tag')
            get_logger().info("从mongodb中得到数据")
            return result
    else:
        return get_logger().error("redis连接失败")


async def merge_two_collection(one_col: str, one_primary: str,
                               two_col: str, two_primary: str,
                               redis_key: str = "lz_merge_data") -> list:
    # import motor
    # import aioredis
    # mongo_client = motor.MotorClient()
    # redis_client = await aioredis.create_redis(('127.0.0.1', '6379'))
    mongo_client = get_handler(TaskKey.mongodb_async)
    redis_client = get_handler(TaskKey.redis_async)
    conn = await redis_client.get_connection()
    if conn:
        db = mongo_client["lz_database"]
        first_col = db[one_col]
        second_col = db[two_col]
        new_col = one_col + '_' + two_col  # 新增集合名称
        redis_key = new_col  # 新增redis的键名
        result = []
        async for i in first_col.aggregate([{"$project": {"_id": 0}}]):
            async for j in second_col.aggregate([{"$project": {"_id": 0}}]):
                if i.get(one_primary, None) and j.get(two_primary, None):  # 主键不存在
                    if i[one_primary] == j[two_primary]:
                        i.update(j)
                        result.append(i)  # 将结果插入返回列表中
                        await db[new_col].insert_one(i)  # 将结果保存到新的集合中
                        break
                else:
                    return []
        new_result = []
        for k in result:
            del k["_id"]
            await conn.lpush(redis_key, str(k))  # 将结果保存至redis中
            new_result.append(k)
        return new_result[0:100]
    else:
        get_logger().error("redis连接失败")


async def get_search_table(first_col, second_col, keyword,
                           locus_tag: str = "Locus_tag",
                           tss_id: str = "TSS_ID"
                           ):
    """得到模糊查询的结果"""
    # import motor
    result = []
    if keyword:
        query = ".*" + str(keyword) + ".*"  # 忽略大小写,查询包括关键字的结果
        query = re.compile(query, re.IGNORECASE)
        # mongo_client = motor.MotorClient()
        mongo_client = get_handler(TaskKey.mongodb_async)
        db = mongo_client["lz_database"]
        new_col = first_col + '_' + second_col  # 新增集合名称
        col = db[new_col]
        async for i in col.find({
            "$or": [{locus_tag: query}, {tss_id: query}]
        }):
            del i["_id"]
            result.append(i)
        return result
    else:
        get_logger().error("搜索没有关键字")
        return []


async def get_search_one(first_col, second_col, keyword,
                         locus_tag: str = "Locus_tag",
                         ):
    """得到精确搜索结果"""
    # import motor
    # mongo_client = motor.MotorClient()
    mongo_client = get_handler(TaskKey.mongodb_async)
    db = mongo_client["lz_database"]
    new_col = first_col + '_' + second_col  # 新增集合名称
    col = db[new_col]
    result = []  # 结果
    i = await col.find_one({locus_tag: keyword})
    del i["_id"]  # 删除id
    for k, v in i.items():
        tmp_dict = {}  # 中间集合
        tmp_dict.update({"key": k, "value": v})
        result.append(tmp_dict)
    return result


async def get_image_json(locus_tag):
    """!!! 数据库标签为locus_tags"""
    """根据locus_tag得到所有的换件比对条件"""
    mongo_client = get_handler(TaskKey.mongodb_async)
    db = mongo_client["lz_database"]
    col = db["padj_log2"]  # padj_log2集合
    result = []
    async for i in col.find({"locus_tags": locus_tag}):
        del i["_id"]  # 删除主键
        result.append(i)
    return result


# 查询用户密码
async def get_user_password(username=None):
    mongo_client = get_handler(TaskKey.mongodb_async)
    db = mongo_client["lz_database"]
    col = db["user_information"]  # 用户信息
    user = await col.find_one({"username": username})
    if user:
        return user['password']
    else:  # 不存在该用户
        return None


# 在菜单中添加数据
async def add_menu(component_name: str, icon: str, code: str):
    """菜单存储collection为mg_menu_info"""
    # import motor
    # mongo_client = motor.MotorClient()
    mongo_client = get_handler(TaskKey.mongodb_async)
    db = mongo_client["lz_database"]
    col = db["mg_menu_info"]
    # 插入一条数据
    res = await col.update_one({"text": component_name, "icon": icon, 'code': code},
                               {"$set": {"text": component_name, "icon": icon, 'code': code}},
                               upsert=True)
    if res.acknowledged:
        return True
    else:
        return False


# 查询菜单中的所有数据
async def get_menu():
    result = []
    mongo_client = get_handler(TaskKey.mongodb_async)
    db = mongo_client["lz_database"]
    col = db["mg_menu_info"]
    async for i in col.find({}):
        del i["_id"]  # 删除主键
        result.append(i)
    return result


async def create_collection_and_index(collection_name: str, indexs: list) -> None:
    """
    创建一个集合，并创建索引
    collection_name: 集合名称
    indexs： 索引名称 [("code", 1), ("item", 1)]
    """
    handle = get_handler(TaskKey.mongodb_async)
    db = handle["lz_database"]
    collection_names = await db.list_collection_names(False)
    if collection_name not in collection_names:
        collection_current = await db.create_collection(collection_name)
        for index in indexs:
            await collection_current.create_index([index])
            get_logger().info("创建集合【%s】和索引【%s】成功", collection_current, index)
    else:
        collection_current = db.get_collection(collection_name)
        for index in indexs:
            await collection_current.create_index([index])
            get_logger().info("得到集合【%s】,创建索引【%s】成功", collection_current, index)


async def get_collection_handle(database_name: str = "lz_database", collection_name: str = ''):
    """
    得到集合处理对象
    """
    handle = get_handler(TaskKey.mongodb_async)
    return handle[database_name].get_collection(collection_name)


async def update_date_access(date: str) -> None:
    """
    更新数据库中，date日的访问次数
    """
    handle = await get_collection_handle(collection_name='access_date')
    await handle.update_one({"date": date}, {"$inc": {"access_num": 1}}, upsert=True)


async def get_date_access():
    """
    得到最近一周的访问量,
    """
    i = datetime.datetime.now()
    month = i.month
    date = i.day
    x_data = ["{}-{}".format(month, date - x) for x in range(6, -1, -1)]  # 得到横坐标
    handle = await get_collection_handle(collection_name="access_date")
    series_data = []
    week_datas = {}  # 一周访问量字典， 考虑后期可以扩展功能
    week_data = []
    for each_data in x_data:
        res = await handle.find_one({"date": each_data})
        if res:
            week_data.append(str(res["access_num"]))  # 每天的访问数量
        else:
            week_data.append("0")
    week_datas.update({"name": '最近一周接口访问量',
                       "type": 'line',
                       "stack": '总量',
                       "areaStyle": {},
                       "data": week_data})
    series_data.append(week_datas)

    res_data = {"x_data": x_data, "series_data": series_data}
    return res_data


async def update_utex_tss_one_data(primary_key, document):
    """
    更新utex_tss的一条数据
    """
    handle = await get_collection_handle(collection_name="tss_utex")
    res = await handle.update_one({'Locus_tags': primary_key}, {"$set": document})
    get_logger().info("更新数据表tss_utex成功%s", res.modified_count)
    return res.raw_result


async def get_all_collection_names():
    """
    得到所有的集合名
    """
    handle = get_handler(TaskKey.mongodb_async)['lz_database']
    lists = await handle.list_collection_names()
    return lists


async def insert_many_data(collection_name: str, data: list):
    """
    在集合中插入多条数据
    """
    handle = await get_collection_handle(collection_name=collection_name)
    res = await handle.insert_many(data)
    return res


async def get_many_data(collection_name: str, filter_name: dict = {}):
    """
    得到集合中的所有文档
    """
    handle = await get_collection_handle(collection_name=collection_name)
    res = []
    async for doc in handle.find(filter_name):
        del doc["_id"]
        res.append(doc)
    return res


async def insert_logging_data(document: dict):
    """
    document的格式：
    {
    "collection_name": 集合名称, str
    "field": 被操作的列名, str
    "old_value": 旧数据, {}
    "new_value": 新数据, {}
    "user": "操作人账号", str
    "username": 操作人姓名 str
    "create_time": 操作时间, str
    "remark": 备注 str
    }
    """
    pass


if __name__ == '__main__':
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(add_menu("导入CSV数据"))
