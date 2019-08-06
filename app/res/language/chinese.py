from .english import English


class Chinese(English):
    l_this = '简体中文'
    unknown = '未知内容: (%s)'
    cancel = '取消'
    ok = '确定'

    node_root = '根节点'
    node_item = '项目'
    node_items = '项目'
    node_none = '（无）'
    node_num = '（%d 个%s）'

    col_key = '键'
    col_type = '类型'
    col_value = '值'

    menu_file = '文件'
    menu_open_file = '打开文件'
    menu_save_file = '保存文件'
    menu_close_file = '关闭文件'

    menu_edit = '编辑'
    menu_undo = '撤销'
    menu_redo = '重做'
    menu_cut = '剪切'
    menu_copy = '复制'
    menu_paste = '粘贴'
    menu_find = '查找'
    menu_replace = '替换'

    menu_languages = '选择语言'
