from app.base.config import ConfigBase


class Config(ConfigBase):
    _protect_fields = [
        'baidu_app_id',
        'baidu_key',
    ]
    baidu_app_id = ''
    baidu_key = ''
