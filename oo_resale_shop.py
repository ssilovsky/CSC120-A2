from computer import *
from typing import Optional

class ResaleShop:


    inventory:list

    def __init__(self):
        self.inventory = []

    
    def buy(self, computer):
        self.inventory.append(computer)
    
    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(item)
        else:
            print("No inventory to display.")

    def sell(self, computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
            print("Item", computer, "sold!")
        else: 
            print("Item", computer, "not found. Please select another item to sell.")


def main():
    comp = Computer("thingy", "boop", 123, 23, "PS4", 2002, 200)
    comp2 = Computer("thy", "bop", 1234, 243, "PS4", 2002, 2004)
    print(vars(comp))
    comp.refurbish("N64")
    print(vars(comp))
    comp.update_price(300)
    # invent = []
    invent = ResaleShop()
    invent.buy(comp)

    
    #invent.sell(1)
    #print(invent)
    invent.print_inventory()


main()

