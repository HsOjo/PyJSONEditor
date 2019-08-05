import platform
import shutil
import sys
from zipfile import ZipFile

from app.res.const import Const
from app.res.language import load_language, LANGUAGES
from app.res.language.translate_language import TranslateLanguage
from tools.translate import *

sys_type = platform.system()
datas = {}


def add_data(src, dest):
    datas[src] = dest


# build translate language data.
common.log('Build', 'Info', 'Building translate data now...')
load_language()
for lang_type in LANGUAGES.values():
    if issubclass(lang_type, TranslateLanguage):
        lang = lang_type()
        if not lang._translated:
            if lang._translate_to == 'cn_t':
                translator = zhconv()
            elif '--translate-baidu' in sys.argv:
                translator = baidu_translate()
            else:
                translator = google_translate()
            common.log('Build', 'Translate', 'Using %s' % translator.__class__.__name__)

            lang.translate(translator)
            lang.save_current_translate()
        add_data(lang._data_path, './app/res/language/translate')

# reset dist directory.
shutil.rmtree('./build', ignore_errors=True)
shutil.rmtree('./dist', ignore_errors=True)

add_data('./app/res/icon.png', './app/res')

data_str = ''
for k, v in datas.items():
    data_str += ' \\\n\t'
    data_str += '--add-data "%s:%s"' % (k, v)

common.log('Build', 'Info', 'Pyinstaller packing now...')

if sys_type == 'Darwin':
    path_icon = './app/res/icon.icns'
else:
    path_icon = './app/res/icon.ico'

pyi_cmd = 'pyinstaller -F -w -n "%s" -i "%s" %s \\\n__main__.py' % (Const.app_name, path_icon, data_str)
print(pyi_cmd)
os.system(pyi_cmd)
os.unlink('./%s.spec' % Const.app_name)
shutil.rmtree('./build', ignore_errors=True)

common.log('Build', 'Info', 'Packing release zip file now...')

# pack release zip file.
if sys_type == 'Darwin':
    zf = ZipFile('./dist/%s-%s.zip' % (Const.app_name, Const.version), 'w')
    src_dir = './dist/%s.app' % Const.app_name
    for d, ds, fs in os.walk(src_dir):
        for f in fs:
            path = os.path.join(d, f)
            z_path = path[7:].strip(os.path.sep)
            zf.write(path, z_path)
        zf.close()

common.log('Build', 'Info', 'Build finish.')