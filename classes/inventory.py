# Demonstration of splitting up a program

from classes import ingredients


class Inventory(object):
    """ Class for Inventory.
        A Dictionary with item names as key and quantity as values.
    """
    def __init__(self, items):
        """ Sets up the Inventory.
            Input is a dictionary with item names as key and quantity as values.
        """
        self.items = items

    def add(self, item, quantity=1):
        """ Adds an item to the inventory.
            Requires item name (string) and quantity (int).
            If quantity not provided, it assumes a default value of 1.
        """
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove(self, item, quantity=1):
        """ Removes an item from the inventory.
            Requires item name (string) and quantity (int).
            If quantity not provided, it assumes a default value of 1.
        """
        if item in self.items:
            if self.items[item] < quantity:
                self.items[item] = 0
            else:
                self.items[item] -= quantity

    def has(self, item):
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

