"""
File: computer.py
Author: Sophia Silovsky
Date: 2024-02
Description: A Python script to create a computer object
"""

from typing import Optional

class Computer:
    # attributes of object Computer 
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

    # method that refurbishes the computer and updates the software
    def refurbish(self, new_os: Optional[str] = None):
        # updating OS is within refurbish method
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
    
    """
    Takes in a new price, updates the price of the associated
    computer if it is the inventory
    """
    def update_price(self, new_price: int):
        print("Changing computer's price...")
        self.price = new_price # update price based on input
        print("Done! The computer now costs", str(new_price) + ".")