# Demonstration of grouping items in lists

def main():
    # Defining the inventory
    inventory = ['flour', 'sugar', 'sausage', 'ham', 'fish', 'crab', 'bamboo shoot', 'lotus head', 'matsutake', 'mushroom',
                 'carrot', 'radish', 'jueyun chili']

    # Greetings
    print("Welcome to One Moon Restaurant\'s Inventory Program.")
    print("*"*20)

    # Inventory check start
    while True:
        # Take input item to check in inventory
        item = input("What item would you like to check?\n[\'q\' to quit]: ")

        # Check for quitting
        if item.strip().lower() == 'q':
            break

        # Inventory check and output
        if item.strip().lower() in inventory:
            print("Yes, we have that item.\n")
        else:
            print("Sorry, we don't have that.\n")

    # Farewell
    print("Have a nice rest of the day.")

    # Termination
    end = input("Press ENTER to close program.")


if __name__ == "__main__":
    main()