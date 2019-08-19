from . import Language


class English(Language):
    l_this = 'English'
    unknown = 'Unknown Str: (%s)'
    cancel = 'Cancel'
    ok = 'OK'
    preferences = 'Preferences'
    untitled = 'Untitled'

    node_root = 'Root'
    node_item = 'Item'
    node_items = 'Items'
    node_none = '-'
    node_num = '(%d %s)'

    col_key = 'Key'
    col_type = 'Type'
    col_value = 'Value'

    menu_file = 'File'
    menu_new_file = 'New File'
    menu_open_file = 'Open File'
    menu_save_file = 'Save File'
    menu_save_file_as = 'Save As...'
    menu_save_file_all = 'Save All'
    menu_close_file = 'Close File'

    menu_edit = 'Edit'
    menu_undo = 'Undo'
    menu_redo = 'Redo'
    menu_cut = 'Cut'
    menu_copy = 'Copy'
    menu_paste = 'Paste'
    menu_find = 'Find'
    menu_replace = 'Replace'

    menu_view = 'View'
    menu_previous_file = 'Previous File'
    menu_next_file = 'Next File'

    menu_languages = 'Languages'

    filter_all = 'All File(*)'
    filter_json = 'JSON File(*.json)'
