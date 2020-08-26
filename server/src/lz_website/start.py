from mg_app_framework import app_start, set_store, set_config_func, set_init_task, TaskKey
from lz_website.config import ConfigStore, InitFunc

from lz_website.util import mongo_connector
from lz_website.util import redis_connector


async def config_process():
    pass


def main(debug_flag=True):
    set_store(ConfigStore())
    set_config_func(config_process)
    set_init_task([
        {TaskKey.mongodb_async: mongo_connector.MongodbConfig()},
        {TaskKey.redis_async: redis_connector.RedisConfig()},
        {TaskKey.init_func: InitFunc()},
    ])

    app_start(debug_flag)
