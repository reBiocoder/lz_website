#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author ：biocoder
# Date   ：2020/3/31 0031 下午 20:59
# *********************************
from mg_app_framework.components import (
    redis_connector
)


class RedisConfig(redis_connector.RedisConfigBasic):
    def get_redis_host(self):
        return '127.0.0.1'

    def get_redis_port(self):
        return '6379'

    def get_redis_password(self):
        return '1234'

    def get_redis_username(self):
        return "zhou"
