from PyQt5.QtWidgets import QApplication, QMessageBox, QFileDialog

from app import common
from .config import Config
from .control import init_app
from .res.const import Const
from .res.language import load_language
from .res.language.english import English
from .util import github


class Application:
    def __init__(self, args):
        common.log('app_init', 'Info', 'version: %s' % Const.version)

        self.qt = QApplication(args)

        Config.load()
        self.lang = None  # type: English
        self.load_language(Config.language)

        self.events = {
            'process_events': self.qt.processEvents,
            'export_log': self.export_log,
            'check_update': self.check_update,
            'load_language': self.load_language,
            'get_language': lambda: self.lang,
        }

    def load_language(self, language):
        self.lang = load_language(language)

    def run(self):
        init_app(events=self.events)
        return self.qt.exec_()

    def callback_exception(self):
        exc = common.get_exception()
        common.log(self.callback_exception, 'Error', exc)

        if QMessageBox.warning(None, self.lang.title_crash, self.lang.description_crash):
            self.export_log()

    def export_log(self):
        [_, folder] = QFileDialog.getExistingDirectory(None, caption=self.lang.menu_export_log)
        if folder is not None:
            log = common.extract_log()
            err = common.extract_err()

            for f in Config._protect_fields:
                v = getattr(Config, f, '')
                if v != '':
                    log = log.replace(v, Const.protector)
                    err = err.replace(v, Const.protector)

            if log != '':
                with open('%s/%s' % (folder, '%s.log' % Const.app_name), 'w') as io:
                    io.write(log)

            if err != '':
                with open('%s/%s' % (folder, '%s.err' % Const.app_name), 'w') as io:
                    io.write(err)

    def check_update(self, test=False):
        try:
            release = github.get_latest_release(Const.author, Const.app_name, timeout=5)
            common.log(self.check_update, 'Info', release)

            if test or common.compare_version(Const.version, release['tag_name']):
                if len(release['assets']) > 0:
                    QMessageBox.information(self.lang.title_check_update, '%s\n%s\n\n%s' % (
                        self.lang.description_new_version, release['body'],
                        release['assets'][0]['browser_download_url']))
                else:
                    QMessageBox.information(self.lang.title_check_update, '%s\n%s\n\n%s' % (
                        self.lang.description_new_version,
                        release['body'], release['assets'][0]['browser_download_url']))
        except:
            common.log(self.check_update, 'Warning', common.get_exception())
