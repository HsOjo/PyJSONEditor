from PyQt5.QtWidgets import QMainWindow, QMenu, QAction

from app.control.main.form import Form
from app.res.const import Const
from app.res.language import LANGUAGES
from app.res.language.english import English
from app.res.view.main.self import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.events = kwargs.get('events')  # type: dict

        self.load_language()
        self.init_languages_menu()

        form = Form(events=self.events)
        form.load_data({'s1': 'test', 'i1': 123, 'f1': 1.23, 'l1': [1, 2, 3], 'd1': {'1': 2, '2': 3}, 'test': None})
        print('dump: %s' % form.dump_data())
        self.tw_content.addTab(form, 'test')

        self.setWindowTitle(Const.app_name)

    @property
    def lang(self):
        return self.events['get_language']()  # type: English

    def load_language(self):
        for key in dir(self):
            item = getattr(self, key)
            if key[0] != '_' and not callable(item):
                if isinstance(item, QMenu):
                    item.setTitle(getattr(self.lang, key.replace('m_', 'menu_', 1)))
                elif isinstance(item, QAction):
                    item.setText(getattr(self.lang, key.replace('a_', 'menu_', 1)))

    def init_languages_menu(self):
        for k in LANGUAGES:
            a_lang = QAction(self)
            a_lang.setText(LANGUAGES[k].l_this)
            a_lang.triggered.connect((lambda x: (lambda _: self.set_language(x)))(k))
            self.m_languages.addAction(a_lang)

    def set_language(self, language):
        self.events['set_language'](language)
        self.load_language()
