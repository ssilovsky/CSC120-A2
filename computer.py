from typing import Optional

class Computer:

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    def __init__(self, description: str, processor_type:str, hard_drive_capacity:int, 
                 memory:int, operating_system:str, year_made:int, price:int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    

    def refurbish(self, new_os: Optional[str] = None):
        if int(self.year_made) < 2000:
            self.price = 0 # too old to sell, donation only
        elif int(self.year_made) < 2012:
            self.price = 250 # heavily-discounted price on machines 10+ years old
        elif int(self.year_made) < 2018:
            self.price = 550 # discounted price on machines 4-to-10 year old machines
        else:
            self.price = 1000 # recent stuff

        if new_os is not None:
            self.operating_system = new_os # update details after installing new OS
    
    def update_price(self, new_price: int):
        print("Changing computer's pice...")
        self.price = new_price
        print("Done! The computer now costs", str(new_price) + ".")