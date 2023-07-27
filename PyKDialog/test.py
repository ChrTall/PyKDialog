import os

from PyKDialog.kdialog import KDialog
from PyKDialog.kdialog_option import KDialogOptionsBuilder

print(KDialog.__doc__)
print(help(KDialogOptionsBuilder().add_option))

# kdialog1 = KDialog() \
#     .combo_box("Choose your fav food", ["Pizza", "Burger", "Chicken"]) \
#     .with_title("Choose") \
#     .with_yes_label("Ja") \
#     .with_no_label("Nein") \
#     .with_ok_label("OK!") \
#     .with_cancel_label("Abbrechen") \
#     .with_continue_label("Weiter")
# kdialog1 = KDialog() \
#     .menu("Order your meal", ["Pizza", "Burger", "Chicken"]) \
#     .with_title("Select Meal")\
#     .with_yes_label("Ja")\
#     .with_no_label("Nein")\
#     .with_ok_label("OK!")\
#     .with_cancel_label("Abbrechen")\
#     .with_continue_label("Weiter")

#kdialog1 = KDialog().check_list("Choose", {"test": "on", "test2": "off", "test3": "on"})
#kdialog1 = KDialog().notification("Well done!", 5)
# kdialog1 = KDialog().icon("firefox")
#
# cmd = kdialog1.build()
#
# print(cmd)
# os.system(cmd)
