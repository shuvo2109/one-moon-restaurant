# Demonstration of grouping items in lists

from classes.inventory import load_inventory
from functions.input_handler import refine_input


def main():
    # Defining the inventory
    inventory = load_inventory()

    # Greetings
    print("Welcome to One Moon Restaurant\'s Inventory Program.")
    print("*"*20)

    # Inventory check start
    while True:
        # Take input item to check in inventory
        item = refine_input(prompt="What item would you like to check?\n[\'q\' to quit]: ", type_=str)

        # Check for quitting
        if item.strip().lower() == 'q':
            break

        # Inventory check and output
        # This does not currently work. Always returns False.
        if inventory.has(item.title()):
            print("Yes, we have that item.\n")
        else:
            print("Sorry, we don't have that.\n")

    # Farewell
    print("\nHave a nice rest of the day.")

    # Termination
    end = input("Press ENTER to close program.")


if __name__ == "__main__":
    main()
