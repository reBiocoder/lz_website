from os.path import dirname, realpath, basename, join
from mg_app_framework import AppConfigBasic, AppType


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
        'app_group': '',
        'app_name': '',
        'app_type': AppType.user,
        'app_version': '',
        'data': {}
    }

    def get_admin_host(self):
        return 'localhost'

    def get_app_port(self):
        return 80
