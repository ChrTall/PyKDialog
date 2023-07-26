from enum import Enum

from PyKDialog.kdialog_option import KDialogCommand


class KDialogOption(Enum):
    TITLE = "--title"
    ICON = "--icon"
    CONTINUE_LABEL = "--continue-label"
    OK_LABEL = "--ok-label"
    CANCEL_LABEL = "--cancel-label"
    YES_LABEL = "--yes-label"
    NO_LABEL = "--no-label"


class KDialog(object):

    def __init__(self):
        self.kdialog_command: KDialogCommand = None
        self.options: dict = {}

    def with_title(self, title: str) -> object:
        self.options.update({KDialogOption.TITLE: title})
        return self

    def with_icon(self, icon: str) -> object:
        self.options.update({KDialogOption.ICON: icon})
        return self

    def with_continue_label(self, continue_label: str) -> object:
        self.options.update({KDialogOption.CONTINUE_LABEL: continue_label})
        return self

    def with_ok_label(self, ok_label: str) -> object:
        self.options.update({KDialogOption.OK_LABEL: ok_label})
        return self

    def with_cancel_label(self, cancel_label: str) -> object:
        self.options.update({KDialogOption.CANCEL_LABEL: cancel_label})
        return self

    def with_yes_label(self, yes_label: str) -> object:
        self.options.update({KDialogOption.YES_LABEL: yes_label})
        return self

    def with_no_label(self, no_label: str) -> object:
        self.options.update({KDialogOption.NO_LABEL: no_label})
        return self

    def yes_no(self, text: str) -> object:
        self.kdialog_command = KDialogCommand("yesno", [text])
        return self

    def yes_no_cancel(self, text: str) -> object:
        self.kdialog_command = KDialogCommand("yesnocancel", [text])
        return self

    def warning_yes_no(self, text: str) -> object:
        self.kdialog_command = KDialogCommand("warningyesno", [text])
        return self

    def warning_yes_no_cancel(self, text: str) -> object:
        self.kdialog_command = KDialogCommand("warningyesnocancel", [text])
        return self

    def warning_continue_cancel(self, text: str) -> object:
        self.kdialog_command = KDialogCommand("warningcontinuecancel", [text])
        return self

    def sorry(self, text: str) -> object:
        self.kdialog_command = KDialogCommand("sorry", [text])
        return self

    def detailed_sorry(self, text: str, details: str) -> object:
        self.kdialog_command = KDialogCommand("detailedsorry", [text, details])
        return self

    def error(self, error: str) -> object:
        self.kdialog_command = KDialogCommand("error", [error])
        return self

    def detailed_error(self, error: str, details: str) -> object:
        self.kdialog_command = KDialogCommand("detailederror", [error, details])
        return self

    def msg_box(self, text: str) -> object:
        self.kdialog_command = KDialogCommand("msgbox", [text])
        return self

    def input_box(self, input_desc: str, init_val: str):
        self.kdialog_command = KDialogCommand("inputbox", [input_desc, init_val])
        return self

    def img_box(self, file_name: str):
        self.kdialog_command = KDialogCommand("imgbox", [file_name])
        return self

    def img_input_box(self, file_name: str, text: str):
        self.kdialog_command = KDialogCommand("imginputbox", [file_name, text])
        return self

    def password(self, description: str):
        self.kdialog_command = KDialogCommand("password", [description])
        return self

    def new_password(self, description: str):
        self.kdialog_command = KDialogCommand("newpassword", [description])
        return self

    def text_box(self, text_file_name: str):
        self.kdialog_command = KDialogCommand("textbox", [text_file_name])
        return self

    def combo_box(self, description: str, selectable_items: list):
        arg_arr = [description]
        for item in selectable_items:
            arg_arr.append(item)
        self.kdialog_command = KDialogCommand("combobox", arg_arr)
        return self

    def menu(self, description: str, menu_items: list):
        arg_arr = [description]
        for index, item in enumerate(menu_items):
            arg_arr.append(index + 1)
            arg_arr.append(item)
        self.kdialog_command = KDialogCommand("menu", arg_arr)
        return self

    def check_list(self, description, entries: dict):
        arg_arr = [description]
        arg_index = 1
        for entry, state in entries.items():
            arg_arr.append(arg_index)
            arg_index += 1
            arg_arr.append(entry)
            arg_arr.append(state)
            self.kdialog_command = KDialogCommand("checklist", arg_arr)
        return self

    def radio_list(self, description: str, entries: dict):
        arg_arr = [description]
        arg_index = 1
        for entry, state in entries.items():
            arg_arr.append(arg_index)
            arg_index += 1
            arg_arr.append(entry)
            arg_arr.append(state)
        self.kdialog_command = KDialogCommand("radiolist", arg_arr)
        return self

    def passive_popup(self, text: str, timeout_in_sec: int):
        self.kdialog_command = KDialogCommand("passivepopup", [text, timeout_in_sec])
        return self

    def notification(self, text: str, timeout_in_sec: int):
        return self.passive_popup(text, timeout_in_sec)

    def get_cmd(self) -> str:
        cmd = 'kdialog'
        for option, value in self.options.items():
            cmd += f' {option.value} "{value}"'
        cmd += f' {self.kdialog_command.get_cmd()}'
        return cmd
