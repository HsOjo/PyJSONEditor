from PyQt5.QtWidgets import QWidget

from app.res.view.form.self import Ui_Form

type_map = {
    str: 'String',
    int: 'Number',
    float: 'Number',
    list: 'Array',
    dict: 'Object',
    bool: 'Boolean',
    None: 'Null',
}
type_map_rev = {}

for k, v in type_map.items():
    type_map_rev[v] = k


class Form(Ui_Form, QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tw_content.setColumnWidth(0, 192)

    def load_data(self, data):
        pass

    def dump_data(self):
        pass
