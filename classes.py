# Demonstration of making classes

# Defining the menu item class
class MenuItem(object):
    # Setting up the menu item
    def __init__(self, title, cost, long_desc='', short_desc='', item_type='main'):
        self.title = title
        self.cost = cost
        self.long_desc = long_desc
        self.short_desc = short_desc
        self.item_type = item_type

    def change_title(self, title):
        self.title = title

    def change_cost(self, cost):
        self.cost = cost

    def change_description(self, long_desc='', short_desc=''):
        if long_desc:
            self.long_desc = long_desc
        if short_desc:
            self.short_desc = short_desc

    def change_item_type(self, item_type):
        self.item_type = item_type

    def print_item(self, desc_type='short'):
        print("{title} ... ${cost}".format(title=self.title, cost=self.cost))
        if desc_type == 'short':
            print(self.short_desc)
        elif desc_type == 'long':
            print(self.long_desc)


# Class menu should encompass all menu items
class Menu(object):
    def __init__(self, breakfast, lunch, dinner):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner

    def print_menu(self):
        print("\nBreakfast:")
        for item in self.breakfast:
            item.print_item()
        print("\nLunch:")
        for item in self.lunch:
            item.print_item()
        print("\nDinner:")
        for item in self.dinner:
            item.print_item()


# Creating a catering class
class CateringItem(MenuItem):
    # CateringItem inheriting from MenuItem because too similar to separate, too different to rewrite
    def __init__(self, title, cost, number_serves, instructions='', long_desc='', short_desc='', item_type='main'):
        super(MenuItem, self).__init__()
        self.title = title
        self.cost = cost
        self.number_serves = number_serves
        self.instructions = instructions
        self.long_desc = long_desc
        self.short_desc = short_desc
        self.item_type = item_type

    def print_item(self, desc_type='short'):
        print("{title} ... ${cost}".format(title=self.title, cost=self.cost))
        print("Serves: {serving_size}".format(serving_size=self.number_serves))
        if desc_type == 'short':
            print(self.short_desc)
        elif desc_type == 'long':
            print(self.long_desc)
        if self.instructions:
            print("Special Instruction: {instruction}".format(instruction=self.instructions))


# Defining the available items as classes
universal_peace = MenuItem(title="Universal Peace",
                           cost=5000,
                           short_desc='Ingredients: Berry, Carrot, Lotus Head, Rice')
squirrel_fish = MenuItem(title="Squirrel Fish",
                         cost=5000,
                         short_desc='Ingredients: Fish, Flour, Sugar, Tomato')
come_and_get_it = MenuItem(title="Come and Get It",
                           cost=5000,
                           short_desc='Ingredients: Fish, Raw Meat, Rice, Tofu')
crystal_shrimp = MenuItem(title='Crystal Shrimp',
                          cost=4500,
                          short_desc='Ingredients: Carrot, Rice, Shrimp Meat')
triple_layered_consomme = MenuItem(title='Triple-Layered Consomme',
                                   cost=4500,
                                   short_desc='Ingredients: Bamboo Shoot, Fowl, Ham')
black_back_perch_stew = MenuItem(title='Black-Back Perch Stew',
                                 cost=4500,
                                 short_desc='Ingredients: Fish, Jueyun Chili, Salt')

# Correct way to define a subclass
universal_peace_2 = CateringItem(title=universal_peace.title,
                                 cost=universal_peace.cost,
                                 number_serves=4,
                                 instructions='Chef Ganyu\'s special: Prosperous Peace',
                                 long_desc=universal_peace.long_desc,
                                 short_desc=universal_peace.short_desc,
                                 item_type=universal_peace.item_type)

# Incorrect way to define a subclass
squirrel_fish_2 = CateringItem(squirrel_fish, cost=squirrel_fish.cost, number_serves=4)


# Setting up the menu
sunday_menu = Menu(breakfast=[universal_peace, crystal_shrimp],
                   lunch=[squirrel_fish, triple_layered_consomme],
                   dinner=[come_and_get_it, black_back_perch_stew])

# Printing the menu to scrutinize everything
sunday_menu.print_menu()
# universal_peace_2.print_item()
# squirrel_fish_2.print_item()
