import pytest

from PyKDialog.kdialog_command import KDialogCommandBuilder, KDialogCommand


class TestKDialogCommand:

    @pytest.mark.parametrize("enum,expected_value", [
        (KDialogCommand.YES_NO, "--yesno"),
        (KDialogCommand.YES_NO_CANCEL, "--yesnocancel"),
        (KDialogCommand.WARNING_YES_NO, "--warningyesno"),
        (KDialogCommand.WARNING_YES_NO_CANCEL, "--warningyesnocancel"),
        (KDialogCommand.WARNING_CONTINUE_CANCEL, "--warningcontinuecancel"),
        (KDialogCommand.SORRY, "--sorry"),
        (KDialogCommand.DETAILED_SORRY, "--detailedsorry"),
        (KDialogCommand.ERROR, "--error"),
        (KDialogCommand.DETAILED_ERROR, "--detailederror"),
        (KDialogCommand.MSG_BOX, "--msgbox"),
        (KDialogCommand.INPUT_BOX, "--inputbox"),
        (KDialogCommand.IMG_BOX, "--imgbox"),
        (KDialogCommand.IMG_INPUT_BOX, "--imginputbox"),
        (KDialogCommand.PASSWORD, "--password"),
        (KDialogCommand.NEW_PASSWORD, "--newpassword"),
        (KDialogCommand.TEXT_BOX, "--textbox"),
        (KDialogCommand.TEXT_INPUT_BOX, "--textinputbox"),
        (KDialogCommand.COMBO_BOX, "--combobox"),
        (KDialogCommand.MENU, "--menu"),
        (KDialogCommand.CHECK_LIST, "--checklist"),
        (KDialogCommand.RADIO_LIST, "--radiolist"),
        (KDialogCommand.PASSIVE_POPUP, "--passivepopup"),
        (KDialogCommand.GET_OPEN_FILENAME, "--getopenfilename"),
        (KDialogCommand.GET_SAVE_FILENAME, "--getsavefilename"),
        (KDialogCommand.GET_EXISTING_DIR, "--getexistingdirectory"),
        (KDialogCommand.GET_OPEN_URL, "--getopenurl"),
        (KDialogCommand.GET_SAVE_URL, "--getsaveurl"),
        (KDialogCommand.GET_ICON, "--geticon"),
        (KDialogCommand.PROGRESSBAR, "--progressbar"),
        (KDialogCommand.GET_COLOR, "--getcolor"),
        (KDialogCommand.DONT_AGAIN, "--dontagain"),
        (KDialogCommand.SLIDER, "--slider"),
        (KDialogCommand.CALENDAR, "--calendar")
    ])
    def test_enum_value(self, enum, expected_value):
        assert enum.value == expected_value


class TestKDialogCommandBuilder:

    def test_kdialog_command_builder(self):
        # arrange
        kdialog_command = KDialogCommand.MSG_BOX
        args = ["Test message"]
        # act
        sut = KDialogCommandBuilder(cmd=kdialog_command, args=args)
        # assert
        assert sut.kdialog_command == kdialog_command
        assert sut.args == args

    def test_build_with_single_arg(self):
        # arrange
        sut = KDialogCommandBuilder(KDialogCommand.MSG_BOX, ["This is a test message"])
        # act
        kdialog_cmd: list = sut.build()
        # assert
        assert kdialog_cmd == ["--msgbox", "This is a test message"]

    def test_build_with_multiple_args(self):
        # arrange
        sut = KDialogCommandBuilder(KDialogCommand.DETAILED_ERROR, ["Invalid Html", "Line 20: <div> element is not "
                                                                                    "closed"])
        # act
        kdialog_cmd: list = sut.build()
        # assert
        assert kdialog_cmd == ["--detailederror", "Invalid Html", "Line 20: <div> element is not closed"]
