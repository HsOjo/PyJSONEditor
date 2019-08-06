from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem

from app.res.language.english import English
from app.res.view.form.self import Ui_Form

type_map = {
    str: 'String',
    int: 'Number',
    float: 'Number',
    list: 'Array',
    dict: 'Object',
    bool: 'Boolean',
    None.__class__: 'Null',
}
type_map_rev = {}

for k, v in type_map.items():
    type_map_rev[v] = k


class Form(Ui_Form, QWidget):

    def __init__(self, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.events = kwargs.get('events')  # type: dict

        self.lang = self.events['get_language']()  # type: English

        self.tw_content.setColumnWidth(0, 192)
        self.tw_content.currentChanged = self._tw_content_currentChanged

        self.items = {}

    def add_item(self, value, key: str = None, parent: QTreeWidgetItem = None):
        if type(value) not in type_map.keys():
            return

        twi = QTreeWidgetItem()
        twi.setText(1, type_map.get(type(value), self.lang.unknown))
        if type(value) in [list, dict]:
            twi.setText(2, '(%s %s)' % (len(value), self.lang.node_items))
            if parent is None:
                twi.setText(0, self.lang.node_root)
                self.tw_content.addTopLevelItem(twi)
            else:
                twi.setText(0, key)
                parent.addChild(twi)

            self.items[id(twi)] = {
                'key': key,
                'value': value,
                'parent': parent,
                'childs': [],
            }
            if isinstance(value, list):
                for child_value in value:
                    self.add_item(key=None, value=child_value, parent=twi)
                self.refresh_array_nums(twi)
            elif isinstance(value, dict):
                for child_key, child_value in value.items():
                    self.add_item(key=child_key, value=child_value, parent=twi)
        elif parent is not None:
            if value is not None:
                twi.setText(2, '%s' % value)
            else:
                twi.setText(2, self.lang.node_none)
            if isinstance(key, str):
                twi.setText(0, key)
            parent.addChild(twi)
            self.items[id(twi)] = {
                'key': key,
                'value': value,
                'parent': parent,
            }

        if parent is not None:
            parent_childs = self.items[id(parent)]  # type:list
            parent_childs['childs'].append(twi)

        return twi

    def refresh_array_nums(self, twi):
        childs = self.items[id(twi)].get('childs')
        if childs is not None:
            child: QTreeWidgetItem
            for index, child in enumerate(childs):
                child.setText(0, '%s %d' % (self.lang.node_item, index))

    def _tw_content_currentChanged(self, new: QModelIndex, old: QModelIndex):
        twi_old = self.tw_content.itemFromIndex(new)  # type:QTreeWidgetItem
        twi_new = self.tw_content.itemFromIndex(new)  # type:QTreeWidgetItem

        if twi_old is not None:
            twi_old.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

        item = self.items.get(id(twi_new))
        if item is not None:
            col = new.column()
            if col == 0 and item['key'] is not None:
                twi_new.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)
            if col == 2 and type(item['value']) not in [list, dict, None]:
                twi_new.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)

    def load_data(self, data):
        twi = self.add_item(data)
        twi.setExpanded(True)

    def dump_data(self, twi: QTreeWidgetItem):
        pass
