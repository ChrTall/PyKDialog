import pytest

from PyKDialog.kdialog_option import KDialogOptionsBuilder, KDialogOption


class TestKDialogOption:
    def test_title_value(self):
        # arrange
        enum = KDialogOption.TITLE
        # act
        enum_val = enum.value
        # assert
        assert enum_val == "--title"

    def test_icon_value(self):
        # arrange
        enum = KDialogOption.ICON
        # act
        enum_val = enum.value
        # assert
        assert enum_val == "--icon"

    def test_continue_label_value(self):
        # arrange
        enum = KDialogOption.CONTINUE_LABEL
        # act
        enum_val = enum.value
        # assert
        assert enum_val == "--continue-label"

    def test_ok_label_value(self):
        # arrange
        enum = KDialogOption.OK_LABEL
        # act
        enum_val = enum.value
        # assert
        assert enum_val == "--ok-label"

    def test_cancel_label_value(self):
        # arrange
        enum = KDialogOption.CANCEL_LABEL
        # act
        enum_val = enum.value
        # assert
        assert enum_val == "--cancel-label"

    def test_yes_label_value(self):
        # arrange
        enum = KDialogOption.YES_LABEL
        # act
        enum_val = enum.value
        # assert
        assert enum_val == "--yes-label"

    def test_no_label_value(self):
        # arrange
        enum = KDialogOption.NO_LABEL
        # act
        enum_val = enum.value
        # assert
        assert enum_val == "--no-label"

    def test_dateformat_value(self):
        # arrange
        enum = KDialogOption.DATEFORMAT
        # act
        enum_val = enum.value
        # assert
        assert enum_val == "--dateformat"

    def test_geometry_value(self):
        # arrange
        enum = KDialogOption.GEOMETRY
        # act
        enum_val = enum.value
        # assert
        assert enum_val == "--geometry"


class TestKDialogOptionsBuilder:
    def test_kdialog_options_builder(self):
        # KDialogOptionsBuilder should not contain options by default
        # act
        sut = KDialogOptionsBuilder()
        # assert
        assert len(sut._KDialogOptionsBuilder__options.keys()) == 0

    def test_add_option_adds_new_option(self):
        # arrange
        sut = KDialogOptionsBuilder()
        # act
        sut.add_option(KDialogOption.TITLE, "Test Title")
        # assert
        assert KDialogOption.TITLE in sut._KDialogOptionsBuilder__options.keys()
        assert sut._KDialogOptionsBuilder__options.get(KDialogOption.TITLE) == "Test Title"

    def test_add_option_updates_existing_option(self):
        # arrange
        sut = KDialogOptionsBuilder()
        sut._KDialogOptionsBuilder__options.update({KDialogOption.ICON: "test-icon"})
        # act
        sut.add_option(KDialogOption.ICON, "updated-test-icon")
        # assert
        assert KDialogOption.ICON in sut._KDialogOptionsBuilder__options.keys()
        assert sut._KDialogOptionsBuilder__options.get(KDialogOption.ICON) == "updated-test-icon"

    def test_add_option_wrong_key(self):
        # arrange
        sut = KDialogOptionsBuilder()
        # act & assert
        with pytest.raises(TypeError) as exception_info:
            sut.add_option("title", "test-title")
        assert exception_info.value.args == ("option: title is not a valid KDialogOption Enum!",)

    def test_remove_option(self):
        # arrange
        sut = KDialogOptionsBuilder()
        sut._KDialogOptionsBuilder__options.update({KDialogOption.ICON: "test-icon"})
        # act
        sut.remove_option(KDialogOption.ICON)
        # assert
        assert KDialogOption.ICON not in sut._KDialogOptionsBuilder__options.keys()

    def test_build_without_options(self):
        # arrange
        sut = KDialogOptionsBuilder()
        # act
        cmd = sut.build()
        # assert
        assert cmd == ''

    def test_build_with_options(self):
        # arrange
        sut = KDialogOptionsBuilder()
        sut.add_option(KDialogOption.TITLE, "test title")
        sut.add_option(KDialogOption.YES_LABEL, "yes label")
        # act
        cmd = sut.build()
        # assert
        assert cmd == ' --title "test title" --yes-label "yes label"'
