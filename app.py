import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

from MainWindow import Ui_MainWindow
# from Win.AddWindow import Ui_add_form
from add_window import AddWindow 
from edit_window import EditWindow

from strap_table import StrapTableModel


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.label = QtWidgets.QLabel()
        self.setupUi(self)
        self.setWindowTitle("LugguageStrapper - 2.0.0")

        #     add windows and setup triggers here
        self.add_window = AddWindow(self)
        self.add_button.clicked.connect(self.open_add_window)
        self.add_window.created_strap.connect(self._add_strap_to_table)

        self.edit_window = EditWindow(self)
        self.edit_button.clicked.connect(self.open_edit_window)
        self.edit_window.edited_strap.connect(self.replace_edited_strap)

        table_headers = ['id', 'name', 'qty', 'colour', 'company code'] 
        self.setup_strap_table(table_headers)

        self.straps = []

    # FURTHER SETUP 
    def setup_strap_table(self, table_headers: list) -> None:
        # self.strap_table.setRowCount(1) 
        self.strap_table.setColumnCount(len(table_headers))
        for i, header in enumerate(table_headers):
            item = QtWidgets.QTableWidgetItem(header)
            self.strap_table.setHorizontalHeaderItem(i, item)

    #   DEFINE WINDOWS AND REPECTIVE OPERATIONS: 
    # 
    #   ADD WINDOW: 
    def open_add_window(self) -> None:
        self.add_window.show()

    def _add_strap_to_table(self, strap: object) -> bool:
        self.straps.append(strap)

        insert_row = self.strap_table.rowCount() 
        self.strap_table.insertRow(insert_row)

        for column, data_piece in enumerate(strap.data_list()):
            print(f'row: {insert_row}, column: {column}, item: {data_piece}')
            item = QtWidgets.QTableWidgetItem(str(data_piece)) 
            self.strap_table.setItem(insert_row, column, item)
        self._extend_cell_functionality()

    # EDIT WINDOW
    def open_edit_window(self) -> None:
        current_table_selction = self.strap_table.selectedIndexes()[-1] 
        for index in self.strap_table.selectedIndexes():
            print(f'index: {index}')
        strap = self.straps[current_table_selction.row()]
        self.edit_window.name_input.setText(strap.name) 
        self.edit_window.qty_selection.setCurrentText(str(strap.qty)) 

        if strap.colour == 'Red':
            self.edit_window.red_radio_button.setChecked(True)
        else:
            self.edit_window.navy_radio_button.setChecked(True)

        if strap.urgent_bool:
            self.edit_window.yes_urgent_radio_button.setChecked(True)
        else:
            self.edit_window.no_urgent_radio_button.setChecked(True)

        if strap.buckle_type == 'Old':
            self.edit_window.old_buckle_radio_button.setChecked(True)
        else: 
            self.edit_window.new_buckle_radio_button.setChecked(True)
        
        self.edit_window.company_code_input.setText(strap.company_code)
        self.edit_window.strap_id = strap.id
        self.edit_window.show()

    def replace_edited_strap(self, strap: object) -> None:
        row_id = strap.id - 1
        print(f'strapId: {strap.id}')
        print(row_id)
        self.straps[row_id] = strap  
        for column, data_piece in enumerate(strap.data_list()):
            item = self.strap_table.item(row_id, column) 
            item.setText(str(data_piece))
        self._extend_cell_functionality()

    def _extend_cell_functionality(self) -> None:
        self.strap_table.cellClicked.connect(self._select_row) 

    def _select_row(self, row: int) -> None:
        # print(f'item: {item}')
        for column in range(self.strap_table.columnCount()):
            row_item = self.strap_table.item(row, column)
            row_item.setSelected(True)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()