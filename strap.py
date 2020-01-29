class Strap:

    id = 1

    def __init__(self, name: str, no_of_repeats: int, 
        qty: int, colour: str, 
        company_code: str, buckle_type: str = None,
        urgent_bool: bool = None) -> object: 

        self.urgent_c_code = 4694

        self.id = Strap.id
        self.name = name 
        self.qty = qty 
        self.colour = colour 
        self.company_code = company_code 
        self.urgent_bool = urgent_bool 
        self.buckle_type = buckle_type
        self.no_of_repeats = no_of_repeats   

        self.check_company_code(company_code)

        Strap.id += 1

    def __str__(self):
        return f'Strap: \n  name: {self.name}'    
    
    def check_company_code(self, company_code: int) -> None:
        if company_code == self.urgent_c_code:
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

         



        