import json
import os

from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem, QComboBox, QCheckBox, QFileDialog

from app.res.language.english import English
from app.res.view.json_editor.self import Ui_Form

type_map = {
    str: 'String',
    float: 'Number',
    int: 'Number',
    list: 'Array',
    dict: 'Object',
    bool: 'Boolean',
    None.__class__: 'Null',
}
type_map_rev = {}
for k, v in type_map.items():
    type_map_rev[v] = k


def json_type_to_python(type_str, data=None, default=None):
    v_type = type_map_rev.get(type_str)
    if data is None:
        return v_type
    else:
        data_type = type(data)
        if isinstance(data, str):
            if v_type == str:
                return data
            elif type_str == 'Number':
                dot_count = data.count('.')
                if dot_count == 0 and data.isnumeric():
                    value = int(data)
                elif dot_count == 1 and data.replace('.', '', 1).isnumeric():
                    value = float(data)
                else:
                    value = default
                return value
            elif v_type == bool:
                return data.lower() not in ['no', 'false', '0', 'none', 'f', 'n']
        elif data_type in [int, float] and type_str == 'Number':
            return data

        try:
            return v_type(data)
        except:
            return default


class JSONEditor(Ui_Form, QWidget):

    def __init__(self, path: str = None, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.events = kwargs.get('events')  # type: dict

        self.load_language()

        self.tw_content.setColumnWidth(0, 192)
        self.tw_content.setColumnWidth(1, 96)
        self.tw_content.setStyleSheet('QTreeWidget::item{height:24px}')

        self.tw_content.currentChanged = self._tw_content_current_changed
        self.tw_content.dataChanged = self._tw_content_data_changed

        self.items = {}
        self.root_twi = None  # type: QTreeWidgetItem
        self.current_twi = None  # type: QTreeWidgetItem

        self._path = path
        self._title = ''

        if path is not None:
            self.load_file(path)

    @property
    def path(self):
        return self._path

    @property
    def title(self):
        return self._title

    def load_file(self, path):
        self._path = path
        self._title = os.path.basename(path)
        with open(path, 'r') as io:
            data = json.load(io)
        self.load_data(data)

    def save_file(self, path=None):
        if path is None:
            path = self._path
        if path is None:
            [path, _] = QFileDialog.getSaveFileName(
                self, caption=self.lang.menu_save_file,
                filter=';;'.join([self.lang.filter_json, self.lang.filter_all]))
        if path is not None:
            data = self.dump_data()
            with open(path, 'w') as io:
                json.dump(data, io, ensure_ascii=False, indent=4)

    @property
    def lang(self):
        language = self.events['get_language']()  # type: English
        return language

    def load_language(self):
        hi = self.tw_content.headerItem()  # type: QTreeWidgetItem
        hi.setText(0, self.lang.col_key)
        hi.setText(1, self.lang.col_type)
        hi.setText(2, self.lang.col_value)

    def g_type_combobox(self, type_str, root=False):
        cb = QComboBox()
        items = [list, dict]
        if not root:
            items.append(self.lang.node_none)
            for item in [str, int, bool, None.__class__]:
                items.append(item)

        items = [type_map.get(item, item) for item in items]
        for index, item in enumerate(items):
            if item == self.lang.node_none:
                cb.insertSeparator(index)
            else:
                cb.insertItem(index, item)
        cb.setCurrentText(type_str)

        return cb

    def show_cb_type(self, twi: QTreeWidgetItem):
        item = self.items.get(id(twi))
        type_str = twi.text(1)

        if item is not None:
            cb = self.g_type_combobox(type_str, item['parent'] is None)
            self.tw_content.setItemWidget(twi, 1, cb)

            def cb_changed(text):
                self.tw_content.removeItemWidget(twi, 1)
                twi.setText(1, text)
                self.callback_item_type_changed(twi, text, type_str)
                self.tw_content.setFocus()
                self.show_cb_type(twi)

            cb.currentTextChanged.connect(cb_changed)
            cb.setFocus()

    def show_cb_boolean_value(self, twi: QTreeWidgetItem):
        item = self.items.get(id(twi))

        if item is not None:
            value = item['value']
            if isinstance(value, bool):
                cb = QCheckBox()
                cb.setText('%s' % value)
                cb.setChecked(value)
                cb.setAutoFillBackground(True)
                self.tw_content.setItemWidget(twi, 2, cb)

                def cb_changed(state):
                    self.tw_content.removeItemWidget(twi, 2)
                    value = bool(state)
                    twi.setText(2, '%s' % value)
                    item['value'] = value
                    self.tw_content.setFocus()
                    self.show_cb_boolean_value(twi)

                cb.stateChanged.connect(cb_changed)
                cb.setFocus()

    def refresh_item_keys(self, twi):
        type_str = twi.text(1)
        item = self.items[id(twi)]  # type: dict
        childs = item.get('childs')

        twi.setText(2, self.lang.node_num % (len(childs), self.lang.node_items))

        if childs is not None:
            child: QTreeWidgetItem
            if type_str == 'Array':
                for index, child in enumerate(childs):
                    key = '%s %d' % (self.lang.node_item, index)
                    child.setText(0, key)
            elif type_str == 'Object':
                for index, child in enumerate(childs):
                    item_child = self.items[id(child)]
                    key = item_child['key']
                    if key is None:
                        key = '%s %d' % (self.lang.node_item, index)
                    item_child['key'] = key
                    child.setText(0, key)

    def callback_item_type_changed(self, twi, new, old):
        item = self.items[id(twi)]  # type: dict
        value_old = item['value']

        v_type_old = json_type_to_python(old)
        v_type_new = json_type_to_python(new)

        if v_type_new not in [list, dict]:
            if v_type_old in [list, dict]:
                childs = item['childs']
                for child in childs:
                    twi.removeChild(child)
                    del self.items[id(child)]
                item['value'] = len(childs)
                del item['childs']
        else:
            if v_type_old not in [list, dict]:
                item['childs'] = []
            self.refresh_item_keys(twi)

        value = '' if old == 'Null' else item['value']
        if new == 'Number':
            value = json_type_to_python(new, value, 0)
        elif v_type_new == bool:
            value = json_type_to_python(new, value, False)
        elif v_type_new == str:
            value = json_type_to_python(new, value, '')
        elif new == 'Null':
            value = None

        item['value'] = value
        if new == 'Null':
            twi.setText(2, self.lang.node_none)
        elif v_type_new not in [list, dict]:
            twi.setText(2, '%s' % value)

        self.callback_item_value_changed(twi, value_old, value)

    def _tw_content_current_changed(self, new: QModelIndex, old: QModelIndex):
        twi_old = self.tw_content.itemFromIndex(old)  # type:QTreeWidgetItem
        twi_new = self.tw_content.itemFromIndex(new)  # type:QTreeWidgetItem
        self.current_twi = twi_new

        if twi_old is not None:
            twi_old.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            # remove item widget will destroy widget.
            self.tw_content.removeItemWidget(twi_old, 1)
            self.tw_content.removeItemWidget(twi_old, 2)

        item = self.items.get(id(twi_new))
        if item is not None:
            type_str = twi_new.text(1)
            v_type = type_map_rev.get(type_str)
            col = new.column()

            parent = item['parent']

            if parent is not None:
                if col == 0 and json_type_to_python(item['parent'].text(1)) == dict:
                    twi_new.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)
                elif col == 2 and v_type not in [list, dict] and type_str != 'Null':
                    if v_type == bool:
                        self.show_cb_boolean_value(twi_new)
                    else:
                        twi_new.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)

            if col == 1:
                self.show_cb_type(twi_new)

    def callback_item_key_changed(self, twi, old, new):
        print('key', old, new)
        print('key', self.dump_data())

    def callback_item_value_changed(self, twi, old, new):
        print('value', old, new)
        print('value', self.dump_data())

    def _tw_content_data_changed(self, qmi: QModelIndex, qmi_1: QModelIndex, roles, p_int=None, *args, **kwargs):
        twi = self.tw_content.itemFromIndex(qmi)  # type:QTreeWidgetItem
        item = self.items[id(twi)]

        if item is not None:
            parent = item['parent']
            if parent is not None:
                parent_type = json_type_to_python(parent.text(1))
            else:
                parent_type = None

            col = qmi.column()
            if col == 0 and parent_type == dict:
                old_key = item['key']
                new_key = twi.text(col)
                if old_key != new_key:
                    item['key'] = new_key
                    self.callback_item_key_changed(twi, old_key, new_key)
            elif col == 2:
                type_str = twi.text(1)
                v_type = json_type_to_python(type_str)

                old_value = item['value']
                new_value_str = twi.text(col)
                new_value = json_type_to_python(type_str, new_value_str, item['value'])

                if v_type not in [list, dict] and type_str != 'Null':
                    if new_value_str == '%s' % new_value:
                        if old_value != new_value:
                            item['value'] = new_value
                            self.callback_item_value_changed(twi, old_value, new_value)
                    else:
                        twi.setText(col, '%s' % old_value)

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

        type_str = type_map.get(v_type, self.lang.node_none)
        twi.setText(1, type_str)

        if v_type in [list, dict]:
            item['childs'] = []
            item['value'] = None

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
            elif isinstance(value, dict):
                for child_key, child_value in value.items():
                    self.add_item(key=child_key, value=child_value, parent=twi)
            self.refresh_item_keys(twi)
        elif parent is not None:
            if value is not None:
                twi.setText(2, '%s' % value)
            else:
                twi.setText(2, self.lang.node_none)
            if isinstance(key, str):
                twi.setText(0, key)

            parent.addChild(twi)
            item['value'] = value
            self.items[id(twi)] = item

        if parent is not None:
            parent_childs = self.items[id(parent)]  # type:list
            parent_childs['childs'].append(twi)

        return twi

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

        key = item['key']
        if v_type in [list, dict]:
            value = v_type()
            for child_twi in item['childs']:
                [k, v] = self.dump_data(child_twi)
                if isinstance(value, list):
                    value.append(v)
                elif isinstance(value, dict):
                    value[k] = v
        else:
            value = item['value']

        if twi == self.root_twi:
            return value
        else:
            return key, value
