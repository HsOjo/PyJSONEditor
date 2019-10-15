import os
import platform
import sys
import traceback
from io import StringIO


def get_exception():
    with StringIO() as io:
        traceback.print_exc(file=io)
        io.seek(0)
        content = io.read()

    return content


def reg_find_one(reg, content, default=''):
    res = reg.findall(content)
    if len(res) > 0:
        return res[0]
    else:
        return default


def get_application_info():
    name = None
    path = None
    if getattr(sys, 'frozen', False):
        name = os.path.basename(sys.executable)
        sys_type = platform.system()
        if sys_type == 'Darwin':
            path = os.path.abspath('%s/../../..' % sys.executable)
        else:
            path = sys.executable

    return name, path


def compare_version(a: str, b: str, ex=False):
    sa = a.split('-')
    sb = b.split('-')

    if ex is False and len(sb) > 1:
        return False
    else:
        return int(sa[0].replace('.', '')) < int(sb[0].replace('.', ''))


def io_read_all(io: StringIO, default=None):
    if io is not None:
        io.seek(0)
        content = io.read()
        io.seek(0, 2)
    else:
        content = default
    return content
