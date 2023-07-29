from unittest.mock import patch

import pytest
from pytest_mock import MockerFixture

from PyKDialog.kdialog import KDialog
from PyKDialog.kdialog_command import KDialogCommandBuilder, KDialogCommand
from PyKDialog.kdialog_option import KDialogOption


# arrange
@pytest.fixture
def kdialog():
    return KDialog()


def test_kdialog(kdialog):
    # act
    command_builder = kdialog.kdialog_command
    options_builder = kdialog.kdialog_command_options
    # assert
    assert command_builder is None
    assert options_builder is not None


def test_get_cmd_includes_options(kdialog):
    # arrange
    kdialog_command_builder = KDialogCommandBuilder(KDialogCommand.YES_NO, ["Yes-No Question"])
    kdialog.kdialog_command = kdialog_command_builder
    kdialog.with_title("Test Title")
    kdialog.with_icon("Test Icon")
    kdialog.with_ok_label("Ok")
    # act
    cmd: list = kdialog._KDialog__get_cmd()
    # assert
    assert cmd == ["kdialog", "--yesno", "Yes-No Question", "--title", "Test Title", "--icon", "Test Icon",
                   "--ok-label", "Ok"]


class TestKDialogOptions:

    # arrange
    @pytest.fixture()
    def spy(self, kdialog, mocker: MockerFixture):
        spy = mocker.spy(kdialog.kdialog_command_options, 'add_option')
        return spy

    def test_with_title(self, kdialog, spy):
        # act
        kdialog.with_title("test title")
        # assert
        spy.assert_called_once_with(KDialogOption.TITLE, "test title")

    def test_with_icon(self, kdialog, spy):
        # act
        kdialog.with_icon("test icon")
        # assert
        spy.assert_called_once_with(KDialogOption.ICON, "test icon")

    def test_with_continue_label(self, kdialog, spy):
        # act
        kdialog.with_continue_label("test continue label")
        # assert
        spy.assert_called_once_with(KDialogOption.CONTINUE_LABEL, "test continue label")

    def test_with_ok_label(self, kdialog, spy):
        # act
        kdialog.with_ok_label("test ok label")
        # assert
        spy.assert_called_once_with(KDialogOption.OK_LABEL, "test ok label")

    def test_with_cancel_label(self, kdialog, spy):
        # act
        kdialog.with_cancel_label("test cancel label")
        # assert
        spy.assert_called_once_with(KDialogOption.CANCEL_LABEL, "test cancel label")

    def test_with_yes_label(self, kdialog, spy):
        # act
        kdialog.with_yes_label("test yes label")
        # assert
        spy.assert_called_once_with(KDialogOption.YES_LABEL, "test yes label")

    def test_with_no_label(self, kdialog, spy):
        # act
        kdialog.with_no_label("test no label")
        # assert
        spy.assert_called_once_with(KDialogOption.NO_LABEL, "test no label")

    def test_with_dateformat(self, kdialog, spy):
        # act todo: better dateformat
        kdialog.with_date_format("my custom dateformat")
        # assert
        spy.assert_called_once_with(KDialogOption.DATEFORMAT, "my custom dateformat")

    def test_with_geometry(self, kdialog, spy):
        # act todo: better geometry
        kdialog.with_geometry("custom geometry")
        # assert
        spy.assert_called_once_with(KDialogOption.GEOMETRY, "custom geometry")


class TestKDialogCommands:

    @pytest.fixture(autouse=True)
    def mock_subprocess_run(self, mocker: MockerFixture):
        patcher = mocker.patch('subprocess.run')
        patcher.start()

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_yes_no(self, mock_class, kdialog):
        # act
        kdialog.yes_no("Test Question")
        # assert
        mock_class.assert_called_once_with(KDialogCommand.YES_NO, ["Test Question"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_yes_no_cancel(self, mock_class, kdialog):
        # act
        kdialog.yes_no_cancel("Test Question")
        # assert
        mock_class.assert_called_once_with(KDialogCommand.YES_NO_CANCEL, ["Test Question"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_warning_yes_no(self, mock_class, kdialog):
        # act
        kdialog.warning_yes_no("Test Question")
        # assert
        mock_class.assert_called_once_with(KDialogCommand.WARNING_YES_NO, ["Test Question"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_warning_yes_no_cancel(self, mock_class, kdialog):
        # act
        kdialog.warning_yes_no_cancel("Test Question")
        # assert
        mock_class.assert_called_once_with(KDialogCommand.WARNING_YES_NO_CANCEL, ["Test Question"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_warning_continue_cancel(self, mock_class, kdialog):
        # act
        kdialog.warning_continue_cancel("Test Question")
        # assert
        mock_class.assert_called_once_with(KDialogCommand.WARNING_CONTINUE_CANCEL, ["Test Question"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_sorry(self, mock_class, kdialog):
        # act
        kdialog.sorry("Test Sorry Message")
        # assert
        mock_class.assert_called_once_with(KDialogCommand.SORRY, ["Test Sorry Message"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_detailed_sorry(self, mock_class, kdialog):
        # act
        kdialog.detailed_sorry("Test Sorry Message", "Test Details")
        # assert
        mock_class.assert_called_once_with(KDialogCommand.DETAILED_SORRY, ["Test Sorry Message", "Test Details"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_error(self, mock_class, kdialog):
        # act
        kdialog.error("Test Error")
        # assert
        mock_class.assert_called_once_with(KDialogCommand.ERROR, ["Test Error"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_detailed_error(self, mock_class, kdialog):
        # act
        kdialog.detailed_error("Test Error", "Test Details")
        # assert
        mock_class.assert_called_once_with(KDialogCommand.DETAILED_ERROR, ["Test Error", "Test Details"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_msg_box(self, mock_class, kdialog):
        # act
        kdialog.msg_box("Test Message")
        # assert
        mock_class.assert_called_once_with(KDialogCommand.MSG_BOX, ["Test Message"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_input_box(self, mock_class, kdialog):
        # act
        kdialog.input_box("Enter your value:", "My initial value")
        # assert
        mock_class.assert_called_once_with(KDialogCommand.INPUT_BOX, ["Enter your value:", "My initial value"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_img_box(self, mock_class, kdialog):
        # act
        kdialog.img_box("file.png")
        # assert
        mock_class.assert_called_once_with(KDialogCommand.IMG_BOX, ["file.png"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_img_input_box(self, mock_class, kdialog):
        # act
        kdialog.img_input_box("file.png", "input_desc")
        # assert
        mock_class.assert_called_once_with(KDialogCommand.IMG_INPUT_BOX, ["file.png", "input_desc"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_password(self, mock_class, kdialog):
        # act
        kdialog.password("Enter password")
        # assert
        mock_class.assert_called_once_with(KDialogCommand.PASSWORD, ["Enter password"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_new_password(self, mock_class, kdialog):
        # act
        kdialog.new_password("Enter new password")
        # assert
        mock_class.assert_called_once_with(KDialogCommand.NEW_PASSWORD, ["Enter new password"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_text_box(self, mock_class, kdialog):
        # act
        kdialog.text_box("test-file.txt")
        # assert
        mock_class.assert_called_once_with(KDialogCommand.TEXT_BOX, ["test-file.txt"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_text_input_box(self, mock_class, kdialog):
        # act
        kdialog.text_input_box("Input Heading", "initial val")
        # assert
        mock_class.assert_called_once_with(KDialogCommand.TEXT_INPUT_BOX, ["Input Heading", "initial val"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_combo_box(self, mock_class, kdialog):
        # act
        kdialog.combo_box("Select best language", ["Python", "Java", "Go", "C#", "C++", "C"])
        # assert
        mock_class.assert_called_once_with(KDialogCommand.COMBO_BOX, ["Select best language", "Python", "Java", "Go", "C#", "C++", "C"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_menu(self, mock_class, kdialog):
        # act
        kdialog.menu("Menu Description", ["Item 1", "Item 2"])
        # assert
        mock_class.assert_called_once_with(KDialogCommand.MENU, ["Menu Description", 1, "Item 1", 2, "Item 2"])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_check_list(self, mock_class, kdialog):
        # arrange
        entries: dict = {"item 1": False, "item 2": True}
        # act
        kdialog.check_list("Check List", entries)
        # assert
        mock_class.assert_called_once_with(KDialogCommand.CHECK_LIST, ["Check List", 1, "item 1", False, 2, "item 2", True])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_radio_list(self, mock_class, kdialog):
        # arrange
        entries: dict = {"item 1": False, "item 2": True}
        # act
        kdialog.radio_list("Radio List", entries)
        # assert
        mock_class.assert_called_once_with(KDialogCommand.RADIO_LIST, ["Radio List", 1, "item 1", False, 2, "item 2", True])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_passive_popup(self, mock_class, kdialog):
        # act
        kdialog.passive_popup("Notification", 5)
        # assert
        mock_class.assert_called_once_with(KDialogCommand.PASSIVE_POPUP, ["Notification", 5])

    @patch('PyKDialog.kdialog.KDialogCommandBuilder', autospec=True)
    def test_notification(self, mock_class, kdialog):
        # act
        kdialog.notification("Notification", 5)
        # assert
        mock_class.assert_called_once_with(KDialogCommand.PASSIVE_POPUP, ["Notification", 5])
