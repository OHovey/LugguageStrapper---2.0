import datetime

from docx import Document 
from docx.shared import Inches

class Papertime:
    def __init__(self, straps: list, strap_colour: str = None):
        self.straps = straps 
        self.strap_colour = strap_colour 
        self.date = datetime.date.today() 
        self.strap_colour = strap_colour

    def make_document(self) -> None:
        document = Document() 
        document.add_heading(f'{self.date} -- {self.strap_colour}') 

        # TODO: fix the argument placement within the map functions
        # DEVIDE BY URGENCY
        # -----------------
        urgent_straps = map(self.straps, lambda strap: strap.urgent_bool) 
        non_urgent_straps = map(self.straps, lambda strap: not strap.urgent_bool) 
        # -----------------
        # DEVIDE BY COLOUR 
        # -----------------
        urgent_red_straps = map(urgent_straps, lambda strap: strap.colour.lower() == 'red') 
        urgent_blue_straps = map(urgent_straps, lambda strap: strap.colour.lower() == 'blue') 

        non_urgent_red_straps = map(non_urgent_straps, lambda strap: strap.colour.lower() == 'red') 
        non_urgent_blue_straps = map(non_urgent_straps, lambda strap: strap.colour.lower() == 'blue') 
        # -----------------
        # DEVIDE BY BUCKLE TYPE 
        # ----------------- 
        urgent_red_straps_NORMLE_BUCKLE = map(urgent_red_straps, lambda strap: strap.buckle_type.lower() == 'new')
        urgent_red_straps_OLD_BUCKLE = map(urgent_red_straps, lambda strap: strap.buckle_type.lower() == 'old')

        urgent_blue_straps_NORMLE_BUCKLE = map(urgent_blue_straps, lambda strap: strap.buckle_type.lower() == 'new')
        urgent_blue_straps_OLD_BUCKLE = map(urgent_blue_straps, lambda strap: strap.buckle_type.lower() == 'old')

        non_urgent_red_straps_NORMLE_BUCKLE = map(urgent_red_straps, lambda strap: strap.buckle_type.lower() == 'new')
        non_urgent_red_straps_OLD_BUCKLE = map(urgent_red_straps, lambda strap: strap.buckle_type.lower() == 'old')

        non_urgent_blue_straps_NORMLE_BUCKLE = map(non_urgent_blue_straps, lambda strap: strap.buckle_type.lower() == 'new')
        non_urgent_blue_straps_OLD_BUCKLE = map(non_urgent_blue_straps, lambda strap: strap.buckle_type.lower() == 'old')
        # -----------------

        blue_index = 0
        red_index = 0

        # Use python-docx library to write out a python document
        if len(urgent_straps): 
            document.add_heading('URGENT') 
            p = document.add_paragraph()

            for strap in urgent_blue_straps_NORMLE_BUCKLE:
                p.add_run(f"{blue_index}B | {strap.qty}X  '{strap.name}' \n").bold() 
                blue_index += 1

            for strap in urgent_blue_straps_OLD_BUCKLE:
                p.add_run(f"{blue_index}B | {strap.qty}X '{strap.name}' {strap.buckle_type} Buckle \n").bold() 
                blue_index += 1 
            
            for strap in urgent_red_straps_NORMLE_BUCKLE:
                p.add_run(f"{red_index}R | {strap.qty}X '{strap.name}' \n") 
                red_index += 1 

            for strap in urgent_red_straps_OLD_BUCKLE:
                p.add_run(f"{red_index}R | {strap.qty}X '{strap.name}' {strap.buckle_type} Buckle \n")
        
        if len(non_urgent_straps):
            document.add_heading('NORMAL') 
            p = document.add_paragraph()

            for strap in non_urgent_blue_straps_NORMLE_BUCKLE:
                p.add_run(f"{blue_index}B | {strap.qty}X  '{strap.name}' \n").bold() 
                blue_index += 1

            for strap in non_urgent_blue_straps_OLD_BUCKLE:
                p.add_run(f"{blue_index}B | {strap.qty}X '{strap.name}' {strap.buckle_type} Buckle \n").bold() 
                blue_index += 1 
            
            for strap in non_urgent_red_straps_NORMLE_BUCKLE:
                p.add_run(f"{red_index}R | {strap.qty}X '{strap.name}' \n") 
                red_index += 1 

            for strap in non_urgent_red_straps_OLD_BUCKLE:
                p.add_run(f"{red_index}R | {strap.qty}X '{strap.name}' {strap.buckle_type} Buckle \n")
        
        if not self.strap_colour:
            document_title = 'All.docx' 
        else:
            document_title = f'{self.strap_colour}.docx'

        document.save() 
            
