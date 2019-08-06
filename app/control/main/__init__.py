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

        form = Form(events=self.events)
        form.load_data({'s1': 'test', 'i1': 123, 'f1': 1.23, 'l1': [1, 2, 3], 'd1': {'1': 2, '2': 3}, 'test': None})
        print('dump: %s'% form.dump_data())
        self.tw_content.addTab(form, 'test')

        self.setWindowTitle(Const.app_name)
