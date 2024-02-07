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
    def __init__(self, description: str, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
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
    
    def update_computer_os(self, computer:dict, new_os:str):
        print("Updating computer OS information...")
        computer['operating_system'] = new_os
        print("Computer OS information updated!")
        return computer
    
def main():
    comp = Computer("thingy", "boop", 123, 23, "PS4", 2002, 200)
    compu = comp.create_computer()
    print(compu)
    comput = comp.update_computer_os(compu, "N64")
    print(comput)

main()