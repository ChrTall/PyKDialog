import subprocess

import pytest

from PyKDialog.kdialog import KDialog

"""
kdialog needs to be installed in order to run these tests.
The dialog describes which actions must be done in order to complete the tests successfully.
"""


@pytest.fixture
def kdialog():
    kd = KDialog()
    kd.with_title("Manual Test: follow the instructions!")
    return KDialog()


def test_yes_no(kdialog):
    # Choose Yes:
    # act
    result_status: int = kdialog.yes_no("Choose yes!")
    # assert
    assert result_status == 0
    # act
    result_status: int = kdialog.yes_no("Choose no!")
    # assert
    assert result_status == 1
    # act
    result_status: int = kdialog.yes_no("Close dialog!")
    # assert
    assert result_status == 2


def test_yes_no_cancel(kdialog):
    # Choose Yes:
    # act
    result_status: int = kdialog.yes_no_cancel("Choose yes!")
    # assert
    assert result_status == 0
    # Choose No:
    # act
    result_status: int = kdialog.yes_no_cancel("Choose no!")
    # assert
    assert result_status == 1
    # Choose cancel:
    # act
    result_status: int = kdialog.yes_no_cancel("Choose cancel!")
    # assert
    assert result_status == 2
    # Close Dialog:
    # act
    result_status: int = kdialog.yes_no_cancel("Close dialog!")
    # assert
    assert result_status == 2


def test_warning_yes_no(kdialog):
    # Choose Yes:
    # act
    result_status: int = kdialog.warning_yes_no("Choose yes!")
    # assert
    assert result_status == 0
    # Choose No:
    # act
    result_status: int = kdialog.warning_yes_no("Choose no!")
    # assert
    assert result_status == 1
    # Close Dialog:
    # act
    result_status: int = kdialog.warning_yes_no("Close dialog!")
    # assert
    assert result_status == 2


def test_warning_yes_no_cancel(kdialog):
    # Choose Yes:
    # act
    result_status: int = kdialog.warning_yes_no_cancel("Choose yes!")
    # assert
    assert result_status == 0
    # Choose No:
    # act
    result_status: int = kdialog.warning_yes_no_cancel("Choose no!")
    # assert
    assert result_status == 1
    # Choose cancel:
    # act
    result_status: int = kdialog.warning_yes_no_cancel("Choose cancel!")
    # assert
    assert result_status == 2
    # Close Dialog:
    # act
    result_status: int = kdialog.warning_yes_no_cancel("Close dialog!")
    # assert
    assert result_status == 2


def test_warning_continue_cancel(kdialog):
    # Choose Continue:
    # act
    result_status: int = kdialog.warning_continue_cancel("Choose Continue!")
    # assert
    assert result_status == 0
    # Choose Cancel:
    # act
    result_status: int = kdialog.warning_continue_cancel("Choose Cancel!")
    # assert
    assert result_status == 1
    # Close Dialog:
    # act
    result_status: int = kdialog.warning_continue_cancel("Close dialog!")
    # assert
    assert result_status == 2


def test_sorry(kdialog):
    # act
    result_status = kdialog.sorry("Choose Ok")
    # assert
    assert result_status == 0
    # act
    result_status = kdialog.sorry("Close Dialog")
    assert result_status == 2


def test_detailed_sorry(kdialog):
    # act
    result_status = kdialog.detailed_sorry("Inspect Details. Then Choose Ok",
                                           "Details of why the action is not possible.")
    # assert
    assert result_status == 0
    # act
    result_status = kdialog.detailed_sorry("Inspect Details. Then Close Dialog",
                                           "Details of why the action is not possible.")
    # assert
    assert result_status == 2


def test_error(kdialog):
    # act
    result_status = kdialog.error("Choose Ok")
    # assert
    assert result_status == 0
    # act
    result_status = kdialog.error("Close Dialog")
    assert result_status == 2


def test_detailed_error(kdialog):
    # act
    result_status = kdialog.detailed_error("Inspect Details. Then Choose Ok", "Details of what caused the error")
    # assert
    assert result_status == 0
    # act
    result_status = kdialog.detailed_error("Inspect Details. Then Close Dialog", "Details of what caused the error")
    # assert
    assert result_status == 2


def test_msg_box(kdialog):
    # act
    result_status = kdialog.msg_box("Click Ok")
    # assert
    assert result_status == 0
    # act
    result_status = kdialog.msg_box("Close Dialog")
    # assert
    assert result_status == 2


def test_input_box(kdialog):
    # act
    res = kdialog.input_box("Don´t change the initial input and click Ok", "test input", exit_on_error=True, exit_msg="Follow the test instructions!")
    # assert
    assert res == "test input"
    # act
    res = kdialog.input_box("Don´t enter input and click Ok", exit_on_error=True, exit_msg="Follow the test instructions!")
    # assert
    assert res == ""
    # act
    with pytest.raises(subprocess.CalledProcessError) as exception_info:
        kdialog.input_box("Click Cancel")
    # act
    with pytest.raises(subprocess.CalledProcessError) as exception_info:
        kdialog.input_box("Close Dialog")


def test_img_box(kdialog):
    # act todo: test how this method works!
    res = kdialog.img_box("test.img")
    print(res)
    # assert
    assert False


def test_img_input_box(kdialog):
    # act todo: test how this method works!
    res = kdialog.img_input_box("test.img", "input description")
    print(res)
    # assert
    assert False


def test_password(kdialog):
    # act
    res = kdialog.password("Enter new password and click Ok. password=test-pwd", exit_on_error=True, exit_msg="Follow the test instructions!")
    # assert
    assert res == "test-pwd"
    # act
    with pytest.raises(subprocess.CalledProcessError) as exception_info:
        kdialog.password("Click Cancel")
    # act
    with pytest.raises(subprocess.CalledProcessError) as exception_info:
        kdialog.password("Close Dialog")



def test_new_password(kdialog):
    # act
    res = kdialog.new_password("Enter new password and click Ok. password=test-pwd", exit_on_error=True, exit_msg="Follow the test instructions!")
    # assert
    assert res == "test-pwd"
    # act
    with pytest.raises(subprocess.CalledProcessError) as exception_info:
        kdialog.new_password("Click Cancel")
    # act
    with pytest.raises(subprocess.CalledProcessError) as exception_info:
        kdialog.new_password("Close Dialog")


def test_text_box(kdialog):
    # act
    txt_filename = "text-box-testdata-ok.txt"
    result_status = kdialog.text_box(txt_filename)
    # assert
    assert result_status == 0
    # act
    txt_filename = "text-box-testdata-close.txt"
    result_status = kdialog.text_box(txt_filename)
    # assert
    assert result_status == 1
    # act
    not_existing_file = "Not-existing-file.txt"
    result_status = kdialog.text_box(not_existing_file)
    # assert
    assert result_status == 255


def test_text_input_box(kdialog):
    # act
    res = kdialog.text_input_box("Do not change the value and click Ok", "test-line-1\ntest-line-2", exit_on_error=True,
                                 exit_msg="Follow the test instructions!")
    # assert
    assert res == "test-line-1\ntest-line-2"
    # act
    res = kdialog.text_input_box("Do not change the value and click Ok", "test-line-1\ntest-line-2", res_as_list=True,
                                 exit_on_error=True, exit_msg="Follow the test instructions!")
    # assert
    assert res == ["test-line-1", "test-line-2"]
    # act
    res = kdialog.text_input_box("Do not enter a value and click Ok", "", exit_on_error=True,
                                 exit_msg="Follow the test instructions!")
    # assert
    assert res == ""
    # act
    res = kdialog.text_input_box("Do not enter a value and click Ok", "", res_as_list=True,
                                 exit_on_error=True, exit_msg="Follow the test instructions!")
    # assert
    assert res == []
    # act
    with pytest.raises(subprocess.CalledProcessError) as exception_info:
        kdialog.text_input_box("Close Dialog", "")

def test_combo_box(kdialog):
    # arrange
    res = kdialog.combo_box("Enter")
    # act

    # assert
