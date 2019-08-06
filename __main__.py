import os
import platform
import sys

from app import Application, common
from app.res.const import Const

# is run at pyinstaller
if getattr(sys, 'frozen', False):
    common.fix_encoding_in_pyinstaller()

    sys_type = platform.system()

    if sys_type == 'Darwin':
        log_dir = os.path.expanduser('~/Library/Logs/')
    elif sys_type == 'Windows':
        log_dir = os.path.expanduser('~/AppData/Local/Temp')
    else:
        log_dir = ''

    path_log = '%s/%s.log' % (log_dir, Const.app_name)
    path_err = '%s/%s.err' % (log_dir, Const.app_name)

    common.io_log = open(path_log, 'w+')
    common.io_err = open(path_err, 'w+')

    # redirect stdout and stderr.
    sys.stdout = common.io_log
    sys.stderr = common.io_err

app = Application(sys.argv)

try:
    status = app.run()
    sys.exit(status)
except SystemExit:
    pass
except:
    app.callback_exception()
