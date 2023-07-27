from enum import Enum

from PyKDialog.kdialog_command import KDialogCommandBuilder, KDialogCommand
from PyKDialog.kdialog_option import KDialogOptionsBuilder, KDialogOption


class KDialog(object):

    def __init__(self) -> None:
        """ Initializes...
        """
        self.kdialog_command: KDialogCommandBuilder = None
        self.kdialog_command_options: KDialogOptionsBuilder = KDialogOptionsBuilder()

    def with_title(self, title: str) -> object:
        self.kdialog_command_options.add_option(KDialogOption.TITLE, title)
        return self

    def with_icon(self, icon: str) -> object:
        self.kdialog_command_options.add_option(KDialogOption.ICON, icon)
        return self

    def with_continue_label(self, continue_label: str) -> object:
        self.kdialog_command_options.add_option(KDialogOption.CONTINUE_LABEL, continue_label)
        return self

    def with_ok_label(self, ok_label: str) -> object:
        self.kdialog_command_options.add_option(KDialogOption.OK_LABEL, ok_label)
        return self

    def with_cancel_label(self, cancel_label: str) -> object:
        self.kdialog_command_options.add_option(KDialogOption.CANCEL_LABEL, cancel_label)
        return self

    def with_yes_label(self, yes_label: str) -> object:
        self.kdialog_command_options.add_option(KDialogOption.YES_LABEL, yes_label)
        return self

    def with_no_label(self, no_label: str) -> object:
        self.kdialog_command_options.add_option(KDialogOption.NO_LABEL, no_label)
        return self

    def with_date_format(self, dateformat: str) -> object:
        self.kdialog_command_options.add_option(KDialogOption.DATEFORMAT, dateformat)
        return self

    def with_geometry(self, geometry: str) -> object:
        self.kdialog_command_options.add_option(KDialogOption.GEOMETRY, geometry)
        return self

    def yes_no(self, text: str) -> object:
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.YES_NO, [text])
        return self

    def yes_no_cancel(self, text: str) -> object:
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.YES_NO_CANCEL, [text])
        return self

    def warning_yes_no(self, text: str) -> object:
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.WARNING_YES_NO, [text])
        return self

    def warning_yes_no_cancel(self, text: str) -> object:
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.WARNING_YES_NO_CANCEL, [text])
        return self

    def warning_continue_cancel(self, text: str) -> object:
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.WARNING_CONTINUE_CANCEL, [text])
        return self

    def sorry(self, text: str) -> object:
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.SORRY, [text])
        return self

    def detailed_sorry(self, text: str, details: str) -> object:
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.DETAILED_SORRY, [text, details])
        return self

    def error(self, error: str) -> object:
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.ERROR, [error])
        return self

    def detailed_error(self, error: str, details: str) -> object:
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.DETAILED_SORRY, [error, details])
        return self

    def msg_box(self, text: str) -> object:
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.MSG_BOX, [text])
        return self

    def input_box(self, input_desc: str, init_val: str):
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.INPUT_BOX, [input_desc, init_val])
        return self

    def img_box(self, file_name: str):
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.IMG_BOX, [file_name])
        return self

    def img_input_box(self, file_name: str, text: str):
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.IMG_INPUT_BOX, [file_name, text])
        return self

    def password(self, description: str):
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.PASSWORD, [description])
        return self

    def new_password(self, description: str):
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.NEW_PASSWORD, [description])
        return self

    def text_box(self, text_file_name: str):
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.TEXT_BOX, [text_file_name])
        return self

    def text_input_box(self, heading: str, init_value: str):
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.TEXT_INPUT_BOX, [heading, init_value])
        return self

    def combo_box(self, description: str, selectable_items: list):
        arg_arr = [description]
        for item in selectable_items:
            arg_arr.append(item)
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.COMBO_BOX, arg_arr)
        return self

    def menu(self, description: str, menu_items: list):
        arg_arr = [description]
        for index, item in enumerate(menu_items):
            arg_arr.append(index + 1)
            arg_arr.append(item)
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.MENU, arg_arr)
        return self

    def check_list(self, description, entries: dict):
        arg_arr = [description]
        arg_index = 1
        for entry, state in entries.items():
            arg_arr.append(arg_index)
            arg_index += 1
            arg_arr.append(entry)
            arg_arr.append(state)
            self.kdialog_command = KDialogCommandBuilder(KDialogCommand.CHECK_LIST, arg_arr)
        return self

    def radio_list(self, description: str, entries: dict):
        arg_arr = [description]
        arg_index = 1
        for entry, state in entries.items():
            arg_arr.append(arg_index)
            arg_index += 1
            arg_arr.append(entry)
            arg_arr.append(state)
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.RADIO_LIST, arg_arr)
        return self

    def passive_popup(self, text: str, timeout_in_sec: int):
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.PASSIVE_POPUP, [text, timeout_in_sec])
        return self

    def notification(self, text: str, timeout_in_sec: int):
        return self.passive_popup(text, timeout_in_sec)

    def get_cmd(self) -> str:
        cmd = 'kdialog'
        cmd += self.kdialog_command_options.build()
        cmd += f' {self.kdialog_command.build()}'
        return cmd
