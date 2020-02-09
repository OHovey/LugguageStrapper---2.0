import sys, os

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

from AddWindow import Ui_add_form
from strap import Strap

class AddWindow(QtWidgets.QMainWindow, Ui_add_form):

    created_strap = QtCore.pyqtSignal(object) 

    def __init__(self, *args, **kwargs):
        super(AddWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle("Add Strap")
        self.ok_button.clicked.connect(self.create_strap)
        self.cancel_button.clicked.connect(self.close)


    def create_strap(self) -> None:
        name = self.name_input.text() 
        qty = self.qty_combo_box.currentText() 
        colour = 'Red' if self.red_radio_button.isChecked() else 'Navy' 
        company_code = self.company_code_input.text() 
        buckle_type = 'New' if self.new_buckle_radio_button.isChecked() else 'Old'
        urgent_bool = True if self.yes_urgent_button.isChecked() else False 
        no_of_repeats = self.repeats_combo_box.currentText() 

        strap = Strap(name, qty, colour, company_code, no_of_repeats, buckle_type, urgent_bool) 

        self.created_strap.emit(strap) 

    def calculate_repeats(self, text: str, qty: int) -> int:
        pass
