# Demonstration of splitting up a program

from one_moon_restaurant.classes import ingredients


class Inventory(object):
    def __init__(self, items):
        self.items = items

    def add(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove(self, item, quantity=1):
        if item in self.items:
            if self.items[item] < quantity:
                print("Can't go negative!")
            else:
                self.items[item] -= quantity

    def has(self, item):
        if item in self.items and self.items[item] != 0:
            return True
        else:
            return False

    def print_inventory(self):
        for item in self.items:
            print("{item} - {quantity}".format(item=item, quantity=self.items[item]))


def load_inventory():
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

    return inventory

