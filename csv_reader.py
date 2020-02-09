import csv
from strap import Strap

class CsvReader:
    def __init__(self, filename):
        self.filename = filename 
        self.header_templates = {'WLUK': [6, 1, 2, 0]}

    def get_data(self) -> list: 
        with open(self.filename, 'r') as readfile:
            print(f'filename: {self.filename}')
            reader = csv.reader(readfile) 
            header_template = self.header_templates.get('WLUK')
            final_data_array = []
            for row in reader:
                if not len(row): 
                    continue
                
                print(f'row: {row}')
                row_of_selected_items = [] 
                for index in header_template:
                    row_of_selected_items.append(row[index]) 
                final_data_array.append(row_of_selected_items)
            readfile.close()
            return final_data_array