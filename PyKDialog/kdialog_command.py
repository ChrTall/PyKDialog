from enum import Enum


class KDialogCommand(Enum):
    """Command that can take multiple arguments and specifies which type of dialog is used.
    """
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
    """Used to build the command with its arguments.
    """

    def __init__(self, cmd: KDialogCommand, args: list) -> None:
        """
        Initializes the builder with the specified command and arguments
        Args:
            cmd (KDialogCommand): the actual kdialog command.
            args (list): the arguments for the command.
        """
        self.__kdialog_command: KDialogCommand = cmd
        self.__args: list = args

    def build(self) -> str:
        """
        Creates a string with the command and the arguments.
        Returns:
            the command fragment of the complete kdialog string.
        """
        cmd = self.__kdialog_command.value
        for arg in self.__args:
            cmd += f' "{arg}"'
        return cmd
