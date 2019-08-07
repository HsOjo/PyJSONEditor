import base64
import json
import os
import platform
import sys

from app import common
from .res.const import Const

sys_type = platform.system()

if sys_type == 'Darwin':
    CONFIG_NAME = ('com.%s.%s' % (Const.author, Const.app_name)).lower()
    CONFIG_FILE = os.path.expanduser('~/Library/Application Support/%s' % CONFIG_NAME)
else:
    CONFIG_NAME = '%s.cfg' % Const.app_name
    CONFIG_FILE = '%s/%s' % (os.path.dirname(sys.executable), CONFIG_NAME)


class Config:
    _protect_fields = [
        'baidu_app_id',
        'baidu_key',
    ]
    language = 'en'
    baidu_app_id = ''
    baidu_key = ''

    @staticmethod
    def load():
        try:
            with open(CONFIG_FILE, 'r') as io:
                config = json.load(io)
                for f in Config._protect_fields:
                    config[f] = base64.b64decode(config[f][::-1].encode()).decode()
                common.dict_to_object(config, Config, new_fields=False)
                common.log('config_load', 'Info', common.object_to_dict(Config))
        except:
            Config.save()

    @staticmethod
    def save():
        with open(CONFIG_FILE, 'w') as io:
            config = common.object_to_dict(Config)
            for f in Config._protect_fields:
                config[f] = base64.b64encode(config[f].encode()).decode()[::-1]
            json.dump(config, io, indent='  ')
            common.log('config_save', 'Info', common.object_to_dict(Config))

    @staticmethod
    def clear():
        if os.path.exists(CONFIG_FILE):
            os.unlink(CONFIG_FILE)
