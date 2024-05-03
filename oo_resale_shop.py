"""
File: oo_resale_shop.py
Author: Sophia Silovsky
Date: 2024-02
Description: A Python script to create a resale shop object and to print the inventory and sell and buy computers
"""

from computer import *
from typing import Optional

class ResaleShop:

    """
    inventory: list to hold shop inventory
    """
    inventory:list

    def __init__(self):
        self.inventory = [] # inventory object created as a list

    """
    Takes in a computer object containing all the information about a computer,
    adds it to the inventory
    """
    def buy(self, computer):
        self.inventory.append(computer) # add Computer class object to list
    
    """
    prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(item)
        else:
            print("No inventory to display.")

    """
    Takes in a computer object, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, computer):
        if computer in self.inventory:
            # if the computer exists in the list, remove the computer
            self.inventory.remove(computer)
            print("Item", computer, "sold!")
        else: 
            print("Item", computer, "not found. Please select another item to sell.")
