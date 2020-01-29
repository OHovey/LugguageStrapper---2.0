
from PyQt5.QtCore import *
from strap import Strap


class StrapTableModel(QAbstractTableModel):
    def __init__(self, parent = None, data = [], *args):
        super(StrapTableModel, self).__init__() 
        self.data = [[0, 'ollie', 4, 'red', 'bndjsncvdj']] 

    def update(self, dataIn: list) -> bool:
        try:
            self.data = dataIn  
            return true 
        except:
            return False 

    def rowCount(self, parent = QModelIndex()) -> int:
        return len(self.data) 
    
    def columnCount(self, parent = QModelIndex) -> int:
        if len(self.data) > 0:
            return len(self.data[0]) 
        return 5 
    
    def data(self, index: QModelIndex = QModelIndex(), role: int = Qt.DisplayRole) -> Strap or QVariant:
        if role == Qt.DisplayRole:
            i = index.row() 
            j = index.column() 
            return self.data[i][j]
        else:
            return QVariant()
        # pass

    def setData(self, index: QModelIndex, value: any, role=Qt.ItemDataRole.EditRole) -> bool:
        try:
            self.data[index.row()] 
        except IndexError:
            self.data.append([])
        
        row = index.row() 
        column = index.column() 

        self.data[row].append(value)
        # print(f'data: {self.data[row]} \n value: {value}')
        # print(f'self.index: {index.row()} : {index.column()}') 
        print(f'indexValid?: {index.isValid()}')
        self.dataChanged.emit(index, index, list())
        return True

    def flags(self, index: QModelIndex) -> Qt.ItemFlags:
        return Qt.ItemIsEditable | Qt.ItemIsEnabled

    

    


