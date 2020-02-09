import re

class Strap:

    id = 1

    urgent_c_code = 4694

    def __init__(self, name: str, 
        qty: int, colour: str, 
        company_code: str, 
        no_of_repeats: int = None,
        buckle_type: str = None,
        urgent_bool: bool = None) -> object: 

        self.id = Strap.id
        self.name = name 
        self.qty = qty 
        self.colour = colour 
        self.company_code = company_code 
        self.urgent_bool = urgent_bool 
        self.buckle_type = buckle_type

        self.check_company_code(company_code)

        self.no_of_repeats = Strap.calculate_repeats(self.name, self.qty)

        Strap.id += 1

    def __str__(self):
        return f'Strap: \n  name: {self.name}'    
    
    def check_company_code(self, company_code: int) -> None:
        if company_code == Strap.urgent_c_code:
            self.buckle = 'Old' 
            self.urgent_bool = True 
            return 

        if self.buckle_type == None:
            self.buckle_type = 'New' 
        if self.urgent_bool == None: 
            self.urgent_bool = False

    def data_list(self) -> list:
        return [
            self.id,
            self.name,
            self.qty,
            self.colour,
            self.company_code
        ]

    @staticmethod
    def calculate_repeats(text: str, qty: int) -> int:
        # these regexes will be used to deduct from the total repeats per strand
        blunt_character_regex = re.compile('[a-zA-Z]') 
        number_regex = re.compile('[0-9]')  
        # these will be used to fo the opposite 
        letter_i = re.compile('[i]+') 
        number_1 = re.compile('[1]+')

        repeat_reducer = 0

        for i in text:
            if blunt_character_regex.match(i):
                return
            if number_regex.match(i):
                return
            repeat_reducer += 1 

            if letter_i.match(i) or number_1.match(i):
                repeat_reducer -= 1 
        
        final_char_length = len(text) - repeat_reducer 

        if final_char_length > 26:
            repeats = 5
        elif final_char_length <= 26 and final_char_length >= 24:
            repeats = 6 
        elif final_char_length >= 20 and final_char_length < 24:
            repeats = 7 
        elif final_char_length >= 16 and final_char_length < 20:
            repeats = 8 
        elif final_char_length >= 12 and final_char_length < 16:
            repeats = 9 
        elif final_char_length >= 9 and final_char_length < 12:
            repeats = 10 
        elif final_char_length >= 6 and final_char_length < 9:
            repeats = 11 
        elif final_char_length == 5:
            repeats = 12 
        elif final_char_length == 4:
            repeats = 13 
        elif final_char_length <= 3:
            repeats == 14  
        
        return repeats * qty
        
        



        