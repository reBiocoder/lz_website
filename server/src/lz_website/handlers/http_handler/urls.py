from mg_app_framework.web import StaticFileBasicHandler
from lz_website.handlers.http_handler.handler import (WebHandler,
                                                      UploadFileHandler, LoginHandler,
                                                      RegisterHandler, IndexHandler,
                                                      IndexColHandler, SearchTableHandler,
                                                      SearchOneHandler, SearchEnvironmentHandler,
                                                      EnvironmentImageHandler, PubmedHandler,
                                                      ColKeyNameHandler, GetOneWeekAccess
                                                      )

from .handler import get_image_upload_path

url = [
    (r'/http_url/', WebHandler),
    (r'/api/upload_csv/', UploadFileHandler),
    (r'/api/login/', LoginHandler),
    (r'/api/register/', RegisterHandler),
    (r'/api/index_data/', IndexHandler),
    (r'/api/index_col/', IndexColHandler),
    (r'/api/search/', SearchTableHandler),
    (r'/api/detail/', SearchOneHandler),
    (r'/api/environment/', SearchEnvironmentHandler),
    (r'/api/get_image/', EnvironmentImageHandler),
    (r'/api/pubmed/', PubmedHandler),
    (r'/api/get_col_keys/', ColKeyNameHandler),
    (r'/api/get_access/', GetOneWeekAccess),
    # 图片静态文件处理
    (r'/api/image/(.*)', StaticFileBasicHandler, {"path": get_image_upload_path()})
]
