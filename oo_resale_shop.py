from computer import *
from typing import Optional

class ResaleShop:


    invetory = []
    itemID:int

    def __init__(self, inventory:list):
        self.inventory = inventory
        self.itemID = 0

    
    def buy(self, computer:dict):
        
        self.itemID += 1 
        self.inventory.append(computer)
        print(self.itemID)
        return self.itemID
    
    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else:
            print("No inventory to display.")

    # def sell(self, computer:dict):
    #     if computer in self.inventory:
    #         del self.inventory[item_id]
    #         print("Item", item_id, "sold!")
    #     else: 
    #         print("Item", item_id, "not found. Please select another item to sell.")

    

def main():
    comp = Computer("thingy", "boop", 123, 23, "PS4", 2002, 200)
    comp2 = Computer("thy", "bop", 1234, 243, "PS4", 2002, 2004)
    print(vars(comp))
    comp.refurbish("N64")
    print(vars(comp))
    comp.update_price(300)
    invent = []
    invent = ResaleShop(invent)
    comput = comp.create_computer()
    comp22 = comp2.create_computer()
    invent.buy(comput)
    invent.buy(comp22)
    print(invent.inventory[[comput]])
    #invent.sell(1)
    #print(invent)
    #invent.print_inventory()


main()

