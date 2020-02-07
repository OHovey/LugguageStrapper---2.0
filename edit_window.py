import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

from EditWindow import Ui_edit_form

from strap import Strap

class EditWindow(QtWidgets.QMainWindow, Ui_edit_form):

    edited_strap = QtCore.pyqtSignal(object)

    def __init__(self, selected_strap: Strap, *args, **kwargs):
        super(EditWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle("Edit Strap")
        self.cancel_button.clicked.connect(self.close) 

        self.ok_button.clicked.connect(self.create_edited_strap)
        # initialize strap id with placeholder value for replacing 
        # during the opening of the edit window
        self.strap_id = 0 

    def create_edited_strap(self) -> None:
        name = self.name_input.text() 
        qty = self.qty_selection.currentText()
        colour = 'Red' if self.red_radio_button.isChecked else 'Navy' 
        company_code = self.company_code_input.text() 
        buckle_type = 'New' if self.new_buckle_radio_button.isChecked else 'Old'
        urgent_bool = True if self.yes_urgent_radio_button else False 
        no_of_repeats = self.repeats_combo_box.currentText()

        strap = Strap(name, no_of_repeats, qty, colour, company_code, buckle_type, urgent_bool) 
        strap.id = self.strap_id
        self.edited_strap.emit(strap)
        
