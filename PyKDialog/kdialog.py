import subprocess
from typing import Union

from PyKDialog.kdialog_command import KDialogCommandBuilder, KDialogCommand
from PyKDialog.kdialog_option import KDialogOptionsBuilder, KDialogOption


class KDialog(object):

    def __init__(self) -> None:
        """ Initializes...
        """
        self.kdialog_command: KDialogCommandBuilder = None
        self.kdialog_command_options: KDialogOptionsBuilder = KDialogOptionsBuilder()

    def with_title(self, title: str):
        """
        Changes the title of the dialog.
        :param title: displayed in the Titlebar of the dialog.
        :type title: str
        :return: the KDialog instance for a fluent api.
        :rtype: KDialog
        """
        self.kdialog_command_options.add_option(KDialogOption.TITLE, title)
        return self

    def with_icon(self, icon: str):
        """
        Changes the icon of the dialog.
        :param icon: displayed in the dialog.
        :type icon: str
        :return: the KDialog instance for a fluent api.
        :rtype: KDialog
        """
        self.kdialog_command_options.add_option(KDialogOption.ICON, icon)
        return self

    def with_continue_label(self, continue_label: str):
        """
        Changes the continue label if the command`s dialog has a continue button.
        :param continue_label: the label of the "continue" button.
        :type continue_label: str
        :return: the KDialog instance for a fluent api.
        :rtype: KDialog
        """
        self.kdialog_command_options.add_option(KDialogOption.CONTINUE_LABEL, continue_label)
        return self

    def with_ok_label(self, ok_label: str):
        """
        Changes the ok label if the command`s dialog has an ok button.
        :param ok_label: the label of the "ok" button.
        :type ok_label: str
        :return: the KDialog instance for a fluent api.
        :rtype: KDialog
        """
        self.kdialog_command_options.add_option(KDialogOption.OK_LABEL, ok_label)
        return self

    def with_cancel_label(self, cancel_label: str):
        """
        Changes the cancel label if the command`s dialog has a cancel button.
        :param cancel_label: the label of the "cancel" button.
        :type cancel_label: str
        :return: the KDialog instance for a fluent api.
        :rtype: KDialog
        """
        self.kdialog_command_options.add_option(KDialogOption.CANCEL_LABEL, cancel_label)
        return self

    def with_yes_label(self, yes_label: str):
        """
        Changes the yes label if the command`s dialog has a yes button.
        :param yes_label: the label of the "yes" button.
        :type yes_label: str
        :return: the KDialog instance for a fluent api.
        :rtype: KDialog
        """
        self.kdialog_command_options.add_option(KDialogOption.YES_LABEL, yes_label)
        return self

    def with_no_label(self, no_label: str):
        """
        Changes the no label if the command`s dialog has a no button.
        :param no_label: the label of the "no" button.
        :type no_label: str
        :return: the KDialog instance for a fluent api.
        :rtype: KDialog
        """
        self.kdialog_command_options.add_option(KDialogOption.NO_LABEL, no_label)
        return self

    def with_date_format(self, dateformat: str):
        """
        Changes the Date format for calendar result and/or default value (Qt-style).
        :param dateformat: Qt-Style dateformat string.
        :type dateformat: str
        :return: the KDialog instance for a fluent api.
        :rtype: KDialog
        """
        self.kdialog_command_options.add_option(KDialogOption.DATEFORMAT, dateformat)
        return self

    def with_geometry(self, geometry: str):
        """
        | Changes the dialog´s geometry.
        | Requires the following format:
        | [=][<width>{xX}<height>][{+-}<xoffset>{+-}<yoffset>]
        :param geometry: geometry string [=][<width>{xX}<height>][{+-}<xoffset>{+-}<yoffset>]
        :type geometry: str
        :return: the KDialog instance for a fluent api.
        :rtype: KDialog
        """
        self.kdialog_command_options.add_option(KDialogOption.GEOMETRY, geometry)
        return self

    def yes_no(self, question: str) -> int:
        """
        | Asks the user the specified question.
        | The user can click the yes, no or x/close button.
        | The returned result status code meaning is the following:
        | 0: if the user clicked on "yes".
        | 1: if the user clicked on "no".
        | 2: if the user closed the dialog with the x/close button.
        :param question: The question that is displayed to the user.
        :type question: str
        :return: the result status code of the dialog.
        :rtype: int
        """
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.YES_NO, [question])
        return self.__invoke_cmd_with_return_code()

    def yes_no_cancel(self, question: str) -> int:
        """
        | Asks the user the specified question.
        | The user can click the yes, no, cancel or x/close button.
        | The returned result status code meaning is the following:
        | 0: if the user clicked on "yes".
        | 1: if the user clicked on "no".
        | 2: if the user clicked on "cancel" or closed the dialog with the x/close button.
        :param question: The question that is displayed to the user.
        :type question: str
        :return: the result status code of the dialog.
        :rtype: int
        """
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.YES_NO_CANCEL, [question])
        return self.__invoke_cmd_with_return_code()

    def warning_yes_no(self, question: str) -> int:
        """
        | Asks the user the specified question with a warning dialog.
        | The user can click the yes, no or x/close button.
        | The returned result status code meaning is the following:
        | 0: if the user clicked on "yes".
        | 1: if the user clicked on "no".
        | 2: if the user closed the dialog with the x/close button.
        :param question: The question that is displayed to the user.
        :type question: str
        :return: the result status code of the dialog.
        :rtype: int
        """
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.WARNING_YES_NO, [question])
        return self.__invoke_cmd_with_return_code()

    def warning_yes_no_cancel(self, question: str) -> int:
        """
        | Asks the user the specified question with a warning dialog.
        | The user can click the yes, no, cancel or x/close button.
        | The returned result status code meaning is the following:
        | 0: if the user clicked on "yes".
        | 1: if the user clicked on "no".
        | 2: if the user clicked on "cancel" or closed the dialog with the x/close button.
        :param question: The question that is displayed to the user.
        :type question: str
        :return: the result status code of the dialog.
        :rtype: int
        """
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.WARNING_YES_NO_CANCEL, [question])
        return self.__invoke_cmd_with_return_code()

    def warning_continue_cancel(self, question: str) -> int:
        """
        | Asks the user if he wants to continue in a warning dialog.
        | The user can click the continue, cancel or x/close button.
        | The returned result status code meaning is the following:
        | 0: if the user clicked on "continue".
        | 1: if the user clicked on "cancel".
        | 2: if the user closed the dialog with the x/close button.
        :param question: The question should be a continue question.
        :type question: str
        :return: the result status code of the dialog.
        :rtype: int
        """
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.WARNING_CONTINUE_CANCEL, [question])
        return self.__invoke_cmd_with_return_code()

    def sorry(self, text: str) -> int:
        """
        | Displays a sorry message to the user.
        | The returned result status code meaning is the following:
        | 0: if the user clicked on "ok".
        | 2: if the user closed the dialog with the x/close button.
        :param text: the sorry message.
        :type text: str
        :return: the result status code of the dialog.
        :rtype: int
        """
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.SORRY, [text])
        return self.__invoke_cmd_with_return_code()

    def detailed_sorry(self, text: str, details: str) -> int:
        """
        | Displays a sorry message with details to the user.
        | The details can be expanded in the dialog and should contain information/technical explanation why
        | the requested action can not be done.
        | The returned result status code meaning is the following:
        | 0: if the user clicked on "ok".
        | 2: if the user closed the dialog with the x/close button.
        :param text: the sorry message.
        :type text: str
        :param details: the details/technical explanation why the requested action can not be executed.
        :type details: str
        :return: the result status code of the dialog.
        :rtype: int
        """
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.DETAILED_SORRY, [text, details])
        return self.__invoke_cmd_with_return_code()

    def error(self, error: str) -> int:
        """
        | Displays an error message to the user.
        | The returned result status code meaning is the following:
        | 0: if the user clicked on "ok".
        | 2: if the user closed the dialog with the x/close button.
        :param error: the error message.
        :type error: str
        :return: the result status code of the dialog.
        :rtype: int
        """
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.ERROR, [error])
        return self.__invoke_cmd_with_return_code()

    def detailed_error(self, error: str, details: str) -> int:
        """
        | Displays a sorry message with details to the user.
        | The details can be expanded in the dialog and should contain information/technical explanation why
        | the requested action can not be done.
        | The returned result status code meaning is the following:
        | 0: if the user clicked on "ok".
        | 2: if the user closed the dialog with the x/close button.
        :param error: the error message.
        :type error: str
        :param details: the details/technical explanation of the error.
        :type details: str
        :return: the result status code of the dialog
        :rtype: int
        """
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.DETAILED_ERROR, [error, details])
        return self.__invoke_cmd_with_return_code()

    def msg_box(self, text: str) -> object:
        """
        | Displays a simple message to the user.
        | The returned result status code meaning is the following:
        | 0: if the user clicked on "ok".
        | 2: if the user closed the dialog with the x/close button.
        :param text: the message that is displayed to the user.
        :type text:
        :return: the result code of the dialog
        :rtype: int
        """
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.MSG_BOX, [text])
        return self.__invoke_cmd_with_return_code()

    def input_box(self, input_desc: str, init_val: str = "", exit_on_error=False, exit_msg=""):
        """
        Single line input box with input_desc as the heading.
        The caller has to validate that the input is not empty or exceeds max-length, etc.
        :param input_desc: describes what the user should enter.
        :type input_desc: str
        :param init_val: optionally set an initial value in the input box.
        :type init_val: str
        :param exit_on_error: default=False, instead-of-raising CalledProcessError an error dialog is shown
            and the program exits with status 1
        :type exit_on_error: bool
        :param exit_msg: if exit_on_error=True,
            optionally customize the error msg that is displayed to the user.
        :type exit_msg: str
        :return: the string that the user entered.
        :rtype: str
        :raises subprocess.CalledProcessError: if the dialog is closed or the user clicked on cancel.
        """
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.INPUT_BOX, [input_desc, init_val])
        if exit_msg == "" and exit_on_error:
            exit_msg = "Program aborted: You must enter a value"
        return self.__get_single_line_str(self.__invoke_cmd_with_return_value(exit_on_error, exit_msg))

    def img_box(self, file_name: str):
        # Todo: test how this method works.
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.IMG_BOX, [file_name])
        return subprocess.run(self.__get_cmd(), capture_output=True, check=True)

    def img_input_box(self, file_name: str, text: str):
        # Todo: test how this method works.
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.IMG_INPUT_BOX, [file_name, text])
        return subprocess.run(self.__get_cmd(), capture_output=True, check=True)

    def password(self, description: str, exit_on_error=False, exit_msg="") -> str:
        """
        Asks the user to enter a password for decryption use cases.
        :param description: the description of the required password.
        :type description: str
        :param exit_on_error: default=False, instead-of-raising CalledProcessError an error dialog is shown
            and the program exits with status 1
        :type exit_on_error: bool
        :param exit_msg: if exit_on_error=True,
            optionally customize the error msg that is displayed to the user.
        :type exit_msg: str
        :return: the password the user entered.
        :rtype: str
        :raises: subprocess.CalledProcessError: if the dialog is closed or the user clicked on cancel.
        """
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.PASSWORD, [description])
        if exit_msg == "" and exit_on_error:
            exit_msg = "Program aborted: You must enter a password"
        return self.__get_single_line_str(self.__invoke_cmd_with_return_value(exit_on_error, exit_msg))

    def new_password(self, description: str, exit_on_error=False, exit_msg=""):
        """
        Asks the user to enter a password with password confirmation for encryption use cases.
        :param description: the description of the required password.
        :type description: str
        :param exit_on_error: default=False, instead-of-raising CalledProcessError an error dialog is shown,
            and the program exits with status 1
        :type exit_on_error: bool
        :param exit_msg: if exit_on_error=True,
            optionally customize the error msg that is displayed to the user.
        :type exit_msg: str
        :return: the password the user entered.
        :rtype: str
        :raises: subprocess.CalledProcessError: if the dialog is closed or the user clicked on cancel.
        """
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.NEW_PASSWORD, [description])
        if exit_msg == "" and exit_on_error:
            exit_msg = "Program aborted: You must enter a password"
        return self.__get_single_line_str(self.__invoke_cmd_with_return_value(exit_on_error, exit_msg))

    def text_box(self, text_file_name: str) -> int:
        """
        | Displays the content of a text file to the user.
        | The returned result status code meaning is the following:
        | 0: if the user clicked on "ok".
        | 1: if the user closed the dialog with the x/close button.
        | 255: if the file was not found.
        :param text_file_name: the filename, absolute path, or relative path of the text file.
        :type text_file_name:
        :return: the result status code of the dialog.
        :rtype: int
        """
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.TEXT_BOX, [text_file_name])
        return self.__invoke_cmd_with_return_code()

    def text_input_box(self, heading: str, init_value: str, res_as_list: bool = False, exit_on_error: bool = False,
                       exit_msg: str = "") -> Union[str, list]:
        """
        Opens a multi-line input in a dialog.
        The Result can be returned as a string with lf or list of lines.
        :param heading: Details about the requested multi-line input.
        :type heading: str
        :param init_value:
        :type init_value:
        :param res_as_list: default=False, optionally return a list of lines.
            Returns an empty list for no content.
        :type res_as_list: bool
        :param exit_on_error: default=False, instead-of-raising CalledProcessError an error dialog is shown,
            and the program exits with status 1
        :type exit_on_error: bool
        :param exit_msg: if exit_on_error=True,
            optionally customize the error msg that is displayed to the user.
        :type exit_msg: str
        :return: the multi-line string or a list of lines.
        :rtype: Union[str, list]
        """
        self.kdialog_command = KDialogCommandBuilder(KDialogCommand.TEXT_INPUT_BOX, [heading, init_value])
        if exit_msg == "" and exit_on_error:
            exit_msg = "Program aborted: You must enter a value"
        return self.__get_multi_line_str(self.__invoke_cmd_with_return_value(exit_on_error, exit_msg), res_as_list)

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

    def __invoke_cmd_with_return_code(self) -> int:
        """
        Invokes the currently stored command with currently stored options.
        The commands return-value is then returned to the caller.
        :return: the commands return-value.
        :rtype: int
        """
        return subprocess.run(self.__get_cmd(), capture_output=True, check=False).returncode

    def __invoke_cmd_with_return_value(self, exit_on_error: bool = False,
                                       error_msg: str = "") -> subprocess.CompletedProcess:
        """
        Invokes the currently stored command with the currently stored options.
        If the command has a non 0 return-value a CalledProcessError is raised.
        :param exit_on_error: default=False, optionally display an error dialog to the user and exit(1) the program.
        :type exit_on_error: bool
        :param error_msg: is displayed in an error dialog if exit_on_error=True,
            and the command returned a non 0 return-value.
        :type error_msg: str
        :return: the CompletedProcess in case no error occurred.
        :rtype: subprocess.CompletedProcess
        :raises subprocess.CalledProcessError
            if the command returned a non 0 return-value and exit_on_error=False.
        """
        if exit_on_error:
            return self.__invoke_with_exit(error_msg)
        else:
            return self.__invoke_without_exit()

    def __invoke_without_exit(self) -> subprocess.CompletedProcess:
        """
        Invokes the command and returns the result.
        In case of an error, a subprocess.CalledProcessError is raised.
        :return: the CompletedProcess in case no error occurred.
        :rtype: subprocess.CompletedProcess
        :raises subprocess.CalledProcessError if the command returned a non 0 return-value.
        """
        return subprocess.run(self.__get_cmd(), capture_output=True, check=True, encoding="utf-8")

    def __invoke_with_exit(self, error_msg: str) -> subprocess.CompletedProcess:
        """
        Invokes the command and in case of an error, the user is notified with an error dialog.
        The method then calls exit(1) to terminate the program.
        :param error_msg: displayed to the user in case of an error.
        :type error_msg: str
        :return: the CompletedProcess in case no error occurred.
        :rtype: subprocess.CompletedProcess
        """
        try:
            return subprocess.run(self.__get_cmd(), capture_output=True, check=True, encoding="utf-8")
        except subprocess.CalledProcessError as ex:
            self.detailed_error(error_msg, str(ex))
            exit(1)

    @staticmethod
    def __get_single_line_str(completed_process: subprocess.CompletedProcess):
        """
        | Should be called in kdialog commands that return a single-line string in stdout.
        | The CompletedProcess must have an utf-8 encoding.
        :param completed_process: the CompletedProcess of the kdialog command.
        :type completed_process: subprocess.CompletedProcess
        :return: the string return value of the kdialog command.
        :rtype: str
        """
        res: str = completed_process.stdout
        if res.endswith("\n"):
            res = res.splitlines()[0]
        return res

    @staticmethod
    def __get_multi_line_str(completed_process: subprocess.CompletedProcess, as_list: bool = False) -> Union[str, list]:
        """
        | Should be called in kdialog commands that return a multi-line string in stdout.
        | The CompletedProcess must have an utf-8 encoding.
        :param completed_process: the CompletedProcess of the kdialog command.
        :type completed_process: subprocess.CompletedProcess
        :param as_list: default=False, optionally return a list of lines.
            Returns an empty list for no content.
        :type as_list: bool
        :return: the multi-line string or a list of lines.
        :rtype: Union[str, list]
        """
        res: str = completed_process.stdout
        if not as_list:
            if res.endswith("\n"):
                res = res.removesuffix("\n")
            return res
        res_line_list = res.splitlines()
        if res_line_list == [""]:
            return []
        return res_line_list

    def __get_cmd(self) -> list:
        """
        Creates the kdialog command args array/lis with the content of the kdialog_command_options
        and the kdialog_command.
        The args array can then be executed with subprocess.run()
        :return: args array/list to execute.
        :rtype: list
        """
        cmd = ['kdialog']
        cmd.extend(self.kdialog_command.build())
        cmd.extend(self.kdialog_command_options.build())
        return cmd
