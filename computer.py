from typing import Optional

class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, processor_type:str, hard_drive_capacity:int, 
                 memory:int, operating_system:str, year_made:int, price:int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need?
    def create_computer(self):
        return {'description': self.description,
                'processor_type': self.processor_type,
                'hard_drive_capacity': self.hard_drive_capacity,
                'memory': self.memory,
                'operating_system': self.operating_system,
                'year_made': self.year_made,
                'price': self.price}
    
    def refurbish(self, computer: dict, new_os: Optional[str] = None):
        if int(computer["year_made"]) < 2000:
            computer["price"] = 0 # too old to sell, donation only
        elif int(computer["year_made"]) < 2012:
            computer["price"] = 250 # heavily-discounted price on machines 10+ years old
        elif int(computer["year_made"]) < 2018:
            computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
        else:
            computer["price"] = 1000 # recent stuff

        if new_os is not None:
            computer["operating_system"] = new_os # update details after installing new OS

    
def main():
    comp = Computer("thingy", "boop", 123, 23, "PS4", 2002, 200)
    compu = comp.create_computer()
    print(compu)
    comput = comp.update_computer_os(compu, "N64")
    print(comput)

main()