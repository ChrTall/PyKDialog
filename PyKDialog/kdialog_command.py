from copy import deepcopy
from enum import Enum


class KDialogCommand(Enum):
    """Command that can take multiple arguments and specifies which type of dialog is used."""
    YES_NO = "--yesno"
    YES_NO_CANCEL = "--yesnocancel"
    WARNING_YES_NO = "--warningyesno"
    WARNING_YES_NO_CANCEL = "--warningyesnocancel"
    WARNING_CONTINUE_CANCEL = "--warningcontinuecancel"
    SORRY = "--sorry"
    DETAILED_SORRY = "--detailedsorry"
    ERROR = "--error"
    DETAILED_ERROR = "--detailederror"
    MSG_BOX = "--msgbox"
    INPUT_BOX = "--inputbox"
    IMG_BOX = "--imgbox"
    IMG_INPUT_BOX = "--imginputbox"
    PASSWORD = "--password"
    NEW_PASSWORD = "--newpassword"
    TEXT_BOX = "--textbox"
    TEXT_INPUT_BOX = "--textinputbox"
    COMBO_BOX = "--combobox"
    MENU = "--menu"
    CHECK_LIST = "--checklist"
    RADIO_LIST = "--radiolist"
    PASSIVE_POPUP = "--passivepopup"
    ######################################
    GET_OPEN_FILENAME = "--getopenfilename"
    GET_SAVE_FILENAME = "--getsavefilename"
    GET_EXISTING_DIR = "--getexistingdirectory"
    GET_OPEN_URL = "--getopenurl"
    GET_SAVE_URL = "--getsaveurl"
    GET_ICON = "--geticon"
    PROGRESSBAR = "--progressbar"
    GET_COLOR = "--getcolor"
    DONT_AGAIN = "--dontagain"
    SLIDER = "--slider"
    CALENDAR = "--calendar"

    # FORMAT only works with color ?
    FORMAT = "--format"
    # DEFAULT only works with Combobox,Menu,Color and Calender
    DEFAULT = "--default"
    # MULTIPLE only works with GET_OPEN_URL and GET_OPEN_FILENAME ?
    MULTIPLE = "--multiple"


class KDialogCommandBuilder(object):
    """Used to build the command with its arguments."""

    def __init__(self, cmd: KDialogCommand, args: list) -> None:
        """Initializes the builder with the specified command and arguments
        :param cmd: the actual kdialog command.
        :type cmd: KDialogCommand
        :param args: the arguments for the command.
        :type args: list
        """
        self.__kdialog_command: KDialogCommand = cmd
        self.__args: list = args

    @property
    def kdialog_command(self) -> KDialogCommand:
        """Getter of the command.
        :return: the command of the builder.
        :rtype: KDialogCommand
        """
        return self.__kdialog_command

    @property
    def args(self) -> list:
        """Readonly copy of the Builders current command args.
        :return: the args of the command.
        :rtype: list
        """
        return deepcopy(self.__args)

    def build(self) -> list:
        """Creates an args list with the command and the arguments.

        :returns: args list fragment of the complete kdialog string.
        :rtype: list
        """
        cmd_args = [self.__kdialog_command.value]
        cmd_args.extend(self.__args)
        return cmd_args
