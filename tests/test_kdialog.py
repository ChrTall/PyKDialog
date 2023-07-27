import pytest

from PyKDialog.kdialog import KDialog
from PyKDialog.kdialog_option import KDialogOptionsBuilder, KDialogOption


@pytest.fixture
def kdialog():
    return KDialog()


def test_kdialog():
    # arrange
    kdialog = KDialog()
    # act
    command_builder = kdialog.kdialog_command
    options_builder = kdialog.kdialog_command_options
    # assert
    assert command_builder is None
    assert options_builder is not None


def test_with_title(kdialog, mocker):
    # arrange
    spy = mocker.spy(kdialog.kdialog_command_options, 'add_option')
    # act
    kdialog.with_title("test title")
    # assert
    spy.assert_called_once_with(KDialogOption.TITLE, "test title")


def test_with_icon(kdialog, mocker):
    # arrange
    spy = mocker.spy(kdialog.kdialog_command_options, 'add_option')
    # act
    kdialog.with_icon("test icon")
    # assert
    spy.assert_called_once_with(KDialogOption.ICON, "test icon")


def test_with_continue_label(kdialog, mocker):
    # arrange
    spy = mocker.spy(kdialog.kdialog_command_options, 'add_option')
    # act
    kdialog.with_continue_label("test continue label")
    # assert
    spy.assert_called_once_with(KDialogOption.CONTINUE_LABEL, "test continue label")


def test_with_ok_label(kdialog, mocker):
    # arrange
    spy = mocker.spy(kdialog.kdialog_command_options, 'add_option')
    # act
    kdialog.with_ok_label("test ok label")
    # assert
    spy.assert_called_once_with(KDialogOption.OK_LABEL, "test ok label")


def test_with_cancel_label(kdialog, mocker):
    # arrange
    spy = mocker.spy(kdialog.kdialog_command_options, 'add_option')
    # act
    kdialog.with_cancel_label("test cancel label")
    # assert
    spy.assert_called_once_with(KDialogOption.CANCEL_LABEL, "test cancel label")


def test_with_yes_label(kdialog, mocker):
    # arrange
    spy = mocker.spy(kdialog.kdialog_command_options, 'add_option')
    # act
    kdialog.with_yes_label("test yes label")
    # assert
    spy.assert_called_once_with(KDialogOption.YES_LABEL, "test yes label")


def test_with_no_label(kdialog, mocker):
    # arrange
    spy = mocker.spy(kdialog.kdialog_command_options, 'add_option')
    # act
    kdialog.with_no_label("test no label")
    # assert
    spy.assert_called_once_with(KDialogOption.NO_LABEL, "test no label")


def test_with_dateformat(kdialog, mocker):
    # arrange
    spy = mocker.spy(kdialog.kdialog_command_options, 'add_option')
    # act todo: better dateformat
    kdialog.with_date_format("my custom dateformat")
    # assert
    spy.assert_called_once_with(KDialogOption.DATEFORMAT, "my custom dateformat")


def test_with_geometry(kdialog, mocker):
    # arrange
    spy = mocker.spy(kdialog.kdialog_command_options, 'add_option')
    # act todo: better geometry
    kdialog.with_geometry("custom geometry")
    # assert
    spy.assert_called_once_with(KDialogOption.GEOMETRY, "custom geometry")
