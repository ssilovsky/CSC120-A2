from computer import *
from typing import Optional

class ResaleShop:


    inventory:list

    def __init__(self):
        self.inventory = [] # inventory object created as a list

    def buy(self, computer):
        self.inventory.append(computer) # add Computer class object to list
    
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
            # if the computer exists in the list, remove the computer
            self.inventory.remove(computer)
            print("Item", computer, "sold!")
        else: 
            print("Item", computer, "not found. Please select another item to sell.")
