#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author ：biocoder
# Date   ：2020/3/30 0030 下午 14:57
# *********************************
from hashlib import md5
import base64
from functools import wraps
import json

from mg_app_framework import MesCode
import lz_website.util.query_util as query


# 制作新密码
def make_password(password=None):
    new_md5 = md5()
    new_md5.update(str(password).encode("utf-8"))
    return base64.b64encode(new_md5.hexdigest().encode("utf-8")).decode("utf-8")


# 验证密码是否正确
def is_authenticated(username, password):
    real_password = query.get_user_password(username)
    if real_password:
        if real_password == make_password(password):  # 密码相等
            return True
        else:
            return False
    else:
        return False


# 设置用户cookie
def set_cookie(username, real_name):
    cookie_result = {"username": username, "real_name": real_name}
    return json.dumps(cookie_result)


def login_required(func):
    async def handler(self, *args, **kwargs):
        cookie = self.get_secure_cookie('session_id')
        if cookie:  # 用户验证成功
            await func(self, *args, **kwargs)
        else:
            self.send_response_data(code=MesCode.login, data={'login_url': 'admin/login/'}, info="请您先登录")
    return handler


if __name__ == '__main__':
    a = make_password("zhoupenghngnng1234dgf56")
    print(a)

