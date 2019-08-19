import os

from PyQt5.QtWidgets import QMainWindow, QMenu, QAction, QFileDialog

from app.config import CONFIG_FILE
from app.control.main.json_editor import JSONEditor
from app.res.const import Const
from app.res.language import LANGUAGES
from app.res.language.english import English
from app.res.view.main.self import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.events = kwargs.get('events')  # type: dict
        self.events.update({
            'set_editor_title': self.set_editor_title,
        })

        self.load_language()
        self.init_languages_menu()

        self.setWindowTitle(Const.app_name)

        self.editors = []
        self.editor_current = None  # type: JSONEditor
        self.open_file(CONFIG_FILE)

        self.tw_content.currentChanged.connect(self._tw_content_current_changed)
        self.a_new_file.triggered.connect(lambda _: self.new_file())
        self.a_open_file.triggered.connect(lambda _: self.open_file())
        self.a_save_file.triggered.connect(lambda _: self.editor_current.save_file())
        self.a_save_file_as.triggered.connect(lambda _: self.editor_current.save_file(save_as=True))
        self.a_save_file_all.triggered.connect(lambda _: [editor.save_file() for editor in self.editors])
        self.a_close_file.triggered.connect(lambda _: self.close_file())
        self.a_previous_file.triggered.connect(
            lambda _: self.tw_content.setCurrentIndex(self.tw_content.currentIndex() - 1))
        self.a_next_file.triggered.connect(
            lambda _: self.tw_content.setCurrentIndex(self.tw_content.currentIndex() + 1))

        self.new_count = 0

    @property
    def lang(self):
        language = self.events['get_language']()  # type: English
        return language

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

    def set_editor_title(self, editor: JSONEditor, title):
        if editor in self.editors:
            index = self.editors.index(editor)
            self.tw_content.setTabText(index, title)

    def _tw_content_current_changed(self, index):
        if 0 <= index < len(self.editors):
            self.editor_current = self.editors[index]

    def add_editor(self, editor, to_current=True):
        self.editors.append(editor)
        self.tw_content.addTab(editor, editor.title)
        if to_current or self.editor_current is None:
            self.tw_content.setCurrentWidget(editor)
            self.editor_current = editor

    def new_file(self):
        self.new_count += 1
        editor = JSONEditor(events=self.events, title='%s %d' % (self.lang.untitled, self.new_count))
        self.add_editor(editor)

    def open_file(self, path=None):
        if path is None:
            [path, _] = QFileDialog.getOpenFileName(
                self, caption=self.lang.menu_open_file,
                filter=';;'.join([self.lang.filter_json, self.lang.filter_all]))
        if path is not None and os.path.exists(path):
            editor = JSONEditor(path, events=self.events)
            self.add_editor(editor)

    def close_file(self):
        if self.editor_current in self.editors:
            index = self.editors.index(self.editor_current)
            self.tw_content.removeTab(index)
            self.editors.remove(self.editor_current)
