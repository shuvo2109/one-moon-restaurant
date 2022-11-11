# Demonstration of splitting up a program
# Demonstration of working with program files

from classes import ingredients
from classes.ingredients import Ingredient


class Inventory(object):
    """ Class for Inventory.
        A Dictionary with item names as key and quantity as values.
    """
    def __init__(self, items: dict):
        """ Sets up the Inventory.
            Input is a dictionary with item names as key and quantity as values.
        """
        self.items = items

    def sort(self):
        """ Sorts the items in the inventory alphabetically (ASCII order)
        """
        sorted_tuple = sorted(self.items.items(), key=lambda x: x[0])
        self.items = dict(sorted_tuple)

    def add(self, item: Ingredient, quantity=1):
        """ Adds an item to the inventory.
            Requires item name (string) and quantity (int).
            If quantity not provided, it assumes a default value of 1.
        """
        if item.title in self.items:
            self.items[item.title] += quantity
        else:
            self.items[item.title] = quantity

        # Sort after adding new item
        self.sort()

    def remove(self, item: Ingredient, quantity=1):
        """ Removes an item from the inventory.
            Requires item name (string) and quantity (int).
            If quantity not provided, it assumes a default value of 1.
        """
        if item.title in self.items:
            if self.items[item.title] < quantity:
                self.items[item.title] = 0
            else:
                self.items[item.title] -= quantity

    def has(self, item: str):
        """ Checks if a particular item is in the inventory.
        """
        if item in self.items and self.items[item] != 0:
            return True
        else:
            return False

    def print_inventory(self):
        """ Prints the current inventory.
            No arguments needed.
        """
        for item in self.items:
            print("{item} - {quantity}".format(item=item, quantity=self.items[item]))


def load_inventory_from_file():
    """ Loads the inventory from inventory.txt file.
        Created only for demonstration purposes.
        Not compatible with other files and hence redundant.
    """
    # Open the file
    file = open('inventory.txt')
    lines = file.readlines()
    items = {}

    # Add items from the file
    for line in lines:
        line = line.strip('\n')
        line = line.split('\t')
        item = Ingredient(title=line[0])
        items[item] = int(line[1])
    inventory = Inventory(items)
    inventory.sort()

    # Close the file
    file.close()

    return inventory


def write_inventory_to_file(inventory: Inventory):
    """ Writes the contents in inventory to inventory.txt file.
        Created only for demonstration purposes.
        Not compatible with other files and hence redundant.
    """
    # Opening the file
    file = open('inventory.txt', 'w')

    # Writing items
    for item in inventory.items:
        file.write("{name}\t{quantity}\n".format(name=item, quantity=inventory.items[item]))

    # Closing the file
    file.close()


def load_inventory():
    """ Used for creating and updating the inventory to be used by other codes.
    """
    # Defining the inventory
    inventory = Inventory(items={})

    # Shipment from 28th October
    inventory.add(ingredients.bamboo_shoot, 3)
    inventory.add(ingredients.carrot, 2)
    inventory.add(ingredients.crab, 1)
    inventory.add(ingredients.ham, 1)
    inventory.add(ingredients.jueyun_chili, 2)
    inventory.add(ingredients.lotus_head, 2)
    inventory.add(ingredients.matsutake, 1)
    inventory.add(ingredients.sugar, 1)

    # Update for 11th November
    inventory.add(ingredients.berry, 1)
    inventory.add(ingredients.crab, 2)
    inventory.add(ingredients.raw_meat, 1)
    inventory.add(ingredients.shrimp_meat, 1)

    inventory.remove(ingredients.bamboo_shoot, 1)
    inventory.remove(ingredients.carrot, 2)
    inventory.remove(ingredients.jueyun_chili, 2)
    inventory.remove(ingredients.lotus_head, 2)

    return inventory
