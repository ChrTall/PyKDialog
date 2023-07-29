from enum import Enum
from copy import deepcopy


class KDialogOption(Enum):
    """Optional Flag that can be added to kdialog cmds."""
    TITLE = "--title"
    """
    Customize the Dialog title.
    """
    ICON = "--icon"
    """
    Specify the popup icon.
    """
    CONTINUE_LABEL = "--continue-label"
    """
    Customize the text of the Continue button label.
    """
    OK_LABEL = "--ok-label"
    """
    Customize the text of the OK button label.
    """
    CANCEL_LABEL = "--cancel-label"
    """
    Customize the text of the Cancel button label.
    """
    YES_LABEL = "--yes-label"
    """
    Customize the text of the Yes button label.
    """
    NO_LABEL = "--no-label"
    """
    Customize the text of the No button label.
    """
    DATEFORMAT = "--dateformat"
    """
    Customize the date format for calendar result
    """
    GEOMETRY = "--geometry"
    """
    Customize the geometry of the Dialog.
    [=][<width>{xX}<height>][{+-}<xoffset>{+-}<yoffset>]
    """


class KDialogOptionsBuilder(object):
    """Used to customize the optional flags of the KDialog Commands."""

    def __init__(self) -> None:
        """Initializes the Builder without any options.
        """
        self.__options: dict = {}

    @property
    def options(self) -> dict:
        """Readonly copy of the Builders current options.
        :return: a copy of the Builders current options.
        :rtype: dict
        """
        return deepcopy(self.__options)

    def add_option(self, option: KDialogOption, val: str) -> None:
        """Adds the given option to the builder.

        :param option: The option/flag that is added to the builder.
        :type option: KDialogOption
        :param val: the value of the option/flag
        :type val: str
        :raises TypeError: if the provided option is not a valid KDialogOption Enum.
        """
        if not isinstance(option, KDialogOption):
            raise TypeError(f"option: {option} is not a valid KDialogOption Enum!")
        self.__options.update({option: val})

    def remove_option(self, option: KDialogOption) -> None:
        """Removes the given option from the builder.

        :param option: the option/flag that is removed.
        :type option: KDialogOption
        :raises TypeError: if the provided option is not a valid KDialogOption Enum.
        """
        if not isinstance(option, KDialogOption):
            raise TypeError(f"option: {option} is not a valid KDialogOption Enum!")
        self.__options.pop(option)

    def build(self) -> list:
        """All added options with their values are combined into an args list.

        :returns: The optional parameters args list of the kdialog cmd.
        :rtype: list
        """
        options = []
        for option, value in self.__options.items():
            options.extend([option.value, value])
        return options
