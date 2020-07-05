#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author ：biocoder
# Date   ：2020/3/26 0026 下午 21:24
# *********************************
from mg_app_framework.components import (
    mongodb_connector
)


class MongodbConfig(mongodb_connector.MongodbConfigBasic):
    def get_mongodb_host(self):
        return '124.70.143.103'

    def get_mongodb_port(self):
        return 27010
