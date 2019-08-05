from PyQt5.QtWidgets import QMainWindow

from app.control.main.form import Form
from app.res.const import Const
from app.res.language.english import English
from app.res.view.main.self import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.events = kwargs.get('events')  # type: dict

        self.lang = self.events['get_language']()  # type: English

        form = Form({'str': 'test', 'int': 123, 'float': 1.23, 'list': [1, 2, 3], 'dict': {'1': 2, '2': 3}})
        self.tw_content.addTab(form, 'test')

        self.setWindowTitle(Const.app_name)
