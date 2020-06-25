from os.path import dirname, realpath, basename, join
from mg_app_framework import AppConfigBasic, AppType, InitFuncBasic, get_logger

from lz_website.util.query_util import create_collection_and_index, get_all_collection_names


class InitFunc(InitFuncBasic):
    async def init_func(self):
        if "access_date" not in await get_all_collection_names():
            get_logger().info("创建访问日志数据库成功")
            await create_collection_and_index(collection_name="access_date", indexs=[("date", 1)])
        if "cyano_genomes" not in await get_all_collection_names():
            get_logger().info("创建cyano_genomes数据库成功")
            await create_collection_and_index(collection_name="cyano_genomes", indexs=[("tax_id", 1)])


class ConfigStore(AppConfigBasic):
    # ==================== DON'T MODIFY THE CODE BETWEEN COMMENT LINE ====================

    work_dir = dirname(dirname(dirname(realpath(__file__))))
    app = basename(dirname(realpath(__file__)))
    log_path = join(work_dir, 'log', app + '.log')
    uuid_path = join(work_dir, '.appid')

    def get_module_dir(self):
        return dirname(realpath(__file__))

    def get_log_path(self):
        return self.log_path

    def get_uuid_path(self):
        return self.uuid_path

    def get_data(self):
        return self.data

    # ==================== DON'T MODIFY THE CODE BETWEEN COMMENT LINE ====================

    data = {
        'app_group': '蓝藻数据库',
        'app_name': '蓝藻数据库',
        'app_type': AppType.user,
        'app_version': '0.0.1',
        'data': {

        }
    }

    def get_admin_host(self):
        return '127.0.0.1'

    def get_app_port(self):
        return 18882

    def connect_admin(self):
        return False