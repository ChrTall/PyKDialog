from PyKDialog.kdialog_command import KDialogCommandBuilder, KDialogCommand


class TestKDialogCommand:
    def test_yes_no_value(self):
        # arrange
        enum = KDialogCommand.YES_NO
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--yesno"

    def test_yes_no_cancel_value(self):
        # arrange
        enum = KDialogCommand.YES_NO_CANCEL
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--yesnocancel"

    def test_warning_yes_no_value(self):
        # arrange
        enum = KDialogCommand.WARNING_YES_NO
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--warningyesno"

    def test_warning_yes_no_cancel_value(self):
        # arrange
        enum = KDialogCommand.WARNING_YES_NO_CANCEL
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--warningyesnocancel"

    def test_warning_continue_cancel_value(self):
        # arrange
        enum = KDialogCommand.WARNING_CONTINUE_CANCEL
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--warningcontinuecancel"

    def test_sorry_value(self):
        # arrange
        enum = KDialogCommand.SORRY
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--sorry"

    def test_detailed_sorry_value(self):
        # arrange
        enum = KDialogCommand.DETAILED_SORRY
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--detailedsorry"

    def test_error_value(self):
        # arrange
        enum = KDialogCommand.ERROR
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--error"

    def test_detailed_error_value(self):
        # arrange
        enum = KDialogCommand.DETAILED_ERROR
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--detailederror"

    def test_msg_box_value(self):
        # arrange
        enum = KDialogCommand.MSG_BOX
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--msgbox"

    def test_input_box_value(self):
        # arrange
        enum = KDialogCommand.INPUT_BOX
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--inputbox"

    def test_img_box_value(self):
        # arrange
        enum = KDialogCommand.IMG_BOX
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--imgbox"

    def test_img_input_box_value(self):
        # arrange
        enum = KDialogCommand.IMG_INPUT_BOX
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--imginputbox"

    def test_password_value(self):
        # arrange
        enum = KDialogCommand.PASSWORD
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--password"

    def test_new_password_value(self):
        # arrange
        enum = KDialogCommand.NEW_PASSWORD
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--newpassword"

    def test_text_box_value(self):
        # arrange
        enum = KDialogCommand.TEXT_BOX
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--textbox"

    def test_text_input_box_value(self):
        # arrange
        enum = KDialogCommand.TEXT_INPUT_BOX
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--textinputbox"

    def test_combo_box_value(self):
        # arrange
        enum = KDialogCommand.COMBO_BOX
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--combobox"

    def test_menu_value(self):
        # arrange
        enum = KDialogCommand.MENU
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--menu"

    def test_check_list_value(self):
        # arrange
        enum = KDialogCommand.CHECK_LIST
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--checklist"

    def test_radio_list_value(self):
        # arrange
        enum = KDialogCommand.RADIO_LIST
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--radiolist"

    def test_passive_popup_value(self):
        # arrange
        enum = KDialogCommand.PASSIVE_POPUP
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--passivepopup"

    def test_get_open_filename_value(self):
        # arrange
        enum = KDialogCommand.GET_OPEN_FILENAME
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--getopenfilename"

    def test_get_save_filename_value(self):
        # arrange
        enum = KDialogCommand.GET_SAVE_FILENAME
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--getsavefilename"

    def test_get_existing_dir_value(self):
        # arrange
        enum = KDialogCommand.GET_EXISTING_DIR
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--getexistingdirectory"

    def test_get_open_url_value(self):
        # arrange
        enum = KDialogCommand.GET_OPEN_URL
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--getopenurl"

    def test_get_save_url_value(self):
        # arrange
        enum = KDialogCommand.GET_SAVE_URL
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--getsaveurl"

    def test_get_icon_value(self):
        # arrange
        enum = KDialogCommand.GET_ICON
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--geticon"

    def test_progressbar_value(self):
        # arrange
        enum = KDialogCommand.PROGRESSBAR
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--progressbar"

    def test_get_color_value(self):
        # arrange
        enum = KDialogCommand.GET_COLOR
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--getcolor"

    def test_dont_again_value(self):
        # arrange
        enum = KDialogCommand.DONT_AGAIN
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--dontagain"

    def test_slider_value(self):
        # arrange
        enum = KDialogCommand.SLIDER
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--slider"

    def test_calendar_value(self):
        # arrange
        enum = KDialogCommand.CALENDAR
        # act
        enum_value = enum.value
        # assert
        assert enum_value == "--calendar"


class TestKDialogCommandBuilder:

    def test_kdialog_command_builder(self):
        # arrange
        kdialog_command = KDialogCommand.MSG_BOX
        args = ["Test message"]
        # act
        sut = KDialogCommandBuilder(cmd=kdialog_command, args=args)
        # assert
        assert sut._KDialogCommandBuilder__kdialog_command == kdialog_command
        assert sut._KDialogCommandBuilder__args == args

    def test_build_with_single_arg(self):
        # arrange
        sut = KDialogCommandBuilder(KDialogCommand.MSG_BOX, ["This is a test message"])
        # act
        kdialog_cmd = sut.build()
        # assert
        assert kdialog_cmd == '--msgbox "This is a test message"'

    def test_build_with_multiple_args(self):
        # arrange
        sut = KDialogCommandBuilder(KDialogCommand.DETAILED_ERROR, ["Invalid Html", "Line 20: <div> element is not "
                                                                                    "closed"])
        # act
        kdialog_cmd = sut.build()
        # assert
        assert kdialog_cmd == '--detailederror "Invalid Html" "Line 20: <div> element is not closed"'
