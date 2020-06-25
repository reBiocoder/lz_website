from mg_app_framework import get_logger
import json


#  更新，删除等敏感操作保存数据库 修饰器
def logging_required(method):
    async def wrapper(self, *args, **kwargs):
        pass
    return wrapper
