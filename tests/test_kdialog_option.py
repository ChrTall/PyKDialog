import pytest

from PyKDialog.kdialog_option import KDialogOptionsBuilder, KDialogOption


class TestKDialogOption:
    @pytest.mark.parametrize("enum,expected_value", [
        (KDialogOption.TITLE, "--title"),
        (KDialogOption.ICON, "--icon"),
        (KDialogOption.CONTINUE_LABEL, "--continue-label"),
        (KDialogOption.OK_LABEL, "--ok-label"),
        (KDialogOption.CANCEL_LABEL, "--cancel-label"),
        (KDialogOption.YES_LABEL, "--yes-label"),
        (KDialogOption.NO_LABEL, "--no-label"),
        (KDialogOption.DATEFORMAT, "--dateformat"),
        (KDialogOption.GEOMETRY, "--geometry")
    ])
    def test_enum_value(self, enum, expected_value):
        assert enum.value == expected_value


class TestKDialogOptionsBuilder:
    def test_kdialog_options_builder(self):
        # KDialogOptionsBuilder should not contain options by default
        # act
        sut = KDialogOptionsBuilder()
        # assert
        assert len(sut.options.keys()) == 0

    def test_add_option_adds_new_option(self):
        # arrange
        sut = KDialogOptionsBuilder()
        # act
        sut.add_option(KDialogOption.TITLE, "Test Title")
        # assert
        assert KDialogOption.TITLE in sut.options.keys()
        assert sut.options.get(KDialogOption.TITLE) == "Test Title"

    def test_add_option_updates_existing_option(self):
        # arrange
        sut = KDialogOptionsBuilder()
        sut.add_option(KDialogOption.ICON, "test-icon")
        # act
        sut.add_option(KDialogOption.ICON, "updated-test-icon")
        # assert
        assert KDialogOption.ICON in sut.options.keys()
        assert sut.options.get(KDialogOption.ICON) == "updated-test-icon"

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
        sut.add_option(KDialogOption.ICON, "test-icon")
        # act
        sut.remove_option(KDialogOption.ICON)
        # assert
        assert KDialogOption.ICON not in sut.options.keys()

    def test_build_without_options(self):
        # arrange
        sut = KDialogOptionsBuilder()
        # act
        cmd: list = sut.build()
        # assert
        assert len(cmd) == 0

    def test_build_with_options(self):
        # arrange
        sut = KDialogOptionsBuilder()
        sut.add_option(KDialogOption.TITLE, "test title")
        sut.add_option(KDialogOption.YES_LABEL, "test yes label")
        # act
        cmd: list = sut.build()
        # assert
        assert cmd == ["--title", "test title", "--yes-label", "test yes label"]
