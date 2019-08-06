from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem, QComboBox

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
        self.tw_content.setColumnWidth(1, 96)
        self.tw_content.setStyleSheet('QTreeWidget::item{height:24px}')

        self.tw_content.currentChanged = self._tw_content_current_changed
        self.tw_content.dataChanged = self._tw_content_data_changed

        self.items = {}
        self.root_twi = None  # type: QTreeWidgetItem

    def g_type_combobox(self, type_str, root=False):
        cb = QComboBox()
        items = [list, dict]
        if not root:
            items.append('-')
            for item in [str, int, bool, None.__class__]:
                items.append(item)

        items = [type_map.get(item, item) for item in items]
        for index, item in enumerate(items):
            if item == '-':
                cb.insertSeparator(index)
            else:
                cb.insertItem(index, item)
        cb.setCurrentText(type_str)

        return cb

    def add_item(self, value, key: str = None, parent: QTreeWidgetItem = None):
        v_type = type(value)
        if v_type not in type_map.keys():
            return

        twi = QTreeWidgetItem()
        item = {
            'key': key,
            'object': twi,
            'parent': parent,
        }

        type_str = type_map.get(v_type, '-')
        twi.setText(1, type_str)

        if v_type in [list, dict]:
            item['childs'] = []
            item['value'] = None

            twi.setText(2, '(%s %s)' % (len(value), self.lang.node_items))
            if parent is None:
                twi.setText(0, self.lang.node_root)
                self.tw_content.addTopLevelItem(twi)
                self.root_twi = twi
            else:
                twi.setText(0, key)
                parent.addChild(twi)

            self.items[id(twi)] = item

            if isinstance(value, list):
                for child_value in value:
                    self.add_item(key=None, value=child_value, parent=twi)
                self.refresh_array_nums(twi)
            elif isinstance(value, dict):
                for child_key, child_value in value.items():
                    self.add_item(key=child_key, value=child_value, parent=twi)
        elif parent is not None:
            if value is not None:
                value = '%s' % value
                item['value'] = value
                twi.setText(2, value)
            else:
                twi.setText(2, self.lang.node_none)
            if isinstance(key, str):
                twi.setText(0, key)
            parent.addChild(twi)
            self.items[id(twi)] = item

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

    def callback_current_type_changed(self, twi, text):
        twi.setText(1, text)

    def _tw_content_current_changed(self, new: QModelIndex, old: QModelIndex):
        twi_old = self.tw_content.itemFromIndex(old)  # type:QTreeWidgetItem
        twi_new = self.tw_content.itemFromIndex(new)  # type:QTreeWidgetItem

        if twi_old is not None:
            twi_old.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            # remove item widget will destroy widget.
            self.tw_content.removeItemWidget(twi_old, 1)

        item = self.items.get(id(twi_new))
        if item is not None:
            type_str = twi_new.text(1)
            v_type = type_map_rev.get(type_str)
            col = new.column()
            if col == 0 and item['key'] is not None:
                twi_new.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)
            elif col == 1:
                cb = self.g_type_combobox(type_str, item['parent'] is None)
                cb.setFixedHeight(24)
                cb.currentTextChanged.connect(lambda text: self.callback_current_type_changed(twi_new, text))
                self.tw_content.setItemWidget(twi_new, 1, cb)
            elif col == 2 and v_type not in [list, dict, None]:
                twi_new.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)

    def _tw_content_data_changed(self, qmi: QModelIndex, qmi_1: QModelIndex, roles, p_int=None, *args, **kwargs):
        twi = self.tw_content.itemFromIndex(qmi)  # type:QTreeWidgetItem

        item = self.items[id(twi)]
        if item is not None:
            col = qmi.column()
            if col == 0:
                old_key = item['key']
                new_key = twi.text(col)
                if old_key is not None and new_key != old_key:
                    item['key'] = new_key
                    print(old_key, new_key)
            elif col == 2:
                old_value = item['value']
                new_value = twi.text(col)
                if new_value != old_value:
                    item['value'] = new_value
                    # print(old_value, new_value)

    def load_data(self, data):
        for item in self.items.values():
            self.tw_content.removeItemWidget(item['object'])
        self.items.clear()
        twi = self.add_item(data)
        twi.setExpanded(True)

    def dump_data(self, twi: QTreeWidgetItem = None):
        if twi is None:
            twi = self.root_twi

        type_str = twi.text(1)
        v_type = type_map_rev.get(type_str)

        item = self.items[id(twi)]  # type: dict
        item = item.copy()

        key = twi.text(0)
        if v_type in [list, dict]:
            value = v_type()
            for child_twi in item['childs']:
                [k, v] = self.dump_data(child_twi)
                if isinstance(value, list):
                    value.append(v)
                elif isinstance(value, dict):
                    value[k] = v
        else:
            value = twi.text(2)
            if type_str == 'Null':
                value = None
            elif type_str == 'Number':
                dot_count = value.count('.')
                if dot_count == 0:
                    value = int(value)
                elif dot_count == 1:
                    value = float(value)

        if twi == self.root_twi:
            return value
        else:
            return key, value
