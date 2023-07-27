from enum import Enum


class KDialogOption(Enum):
    """Optional Flag that can be added to kdialog cmds.
    """
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
    """Used to customize the optional flags of the KDialog Commands.
    """

    def __init__(self) -> None:
        """Initializes the Builder without any options.
        """
        self.__options: dict = {}

    def add_option(self, option: KDialogOption, val: str) -> None:
        """Adds the given option to the builder.

        Args:
            option (KDialogOption): The option/flag that should be added to the builder.
            val (str): The value of the option/flag
        Raises:
            TypeError: if the provided option is not a valid KDialogOption Enum.
        """
        if not isinstance(option, KDialogOption):
            raise TypeError(f"option: {option} is not a valid KDialogOption Enum!")
        self.__options.update({option: val})

    def remove_option(self, option: KDialogOption) -> None:
        """Removes the given option from the builder.

        Args:
            option (KDialogOption): The option/flag that should be removed from the builder.
        Raises:
            TypeError: if the provided option is not a valid KDialogOption Enum.
        """
        if not isinstance(option, KDialogOption):
            raise TypeError(f"option: {option} is not a valid KDialogOption Enum!")
        self.__options.pop(option)

    def build(self) -> str:
        """All added options with their values are combined into a string.
        The string is a fragment of the complete kdialog cmd.
        Returns:
             The optional parameters fragment of the kdialog cmd.
        """
        options = ''
        for option, value in self.__options.items():
            options += f' {option.value} "{value}"'
        return options
