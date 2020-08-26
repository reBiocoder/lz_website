#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author ：biocoder
# Date   ：2020/3/31 0031 下午 21:12
# *********************************
from mg_app_framework import (get_handler, get_logger, TaskKey
                              )
import json


async def insert_data(key: str, data: dict) -> bool:
    """
    在key中插入一条数据
    :param key:
    :param data:
    :return:
    """
    # import aioredis
    # connection = await aioredis.create_redis(('localhost', 6379),encoding='utf-8')
    redis_handler = get_handler(TaskKey.redis_async)
    await redis_handler.get_connection()
    if redis_handler.get_connection:
        try:
            await redis_handler.get_connection.lpush(key, json.dumps(data))
            return True
        except Exception as e:
            get_logger().error("redis插入数据错误：%s" % e)
            return False
    else:
        return False


async def get_data(key: str) -> list:
    redis_handler = get_handler(TaskKey.redis_async)
    await redis_handler.get_connection()
    if redis_handler.get_connection:
        data = await redis_handler.get_connection.lrange(key, 0, -1)
        return data
    else:
        return []

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(insert_list([1,2,3,4]))
