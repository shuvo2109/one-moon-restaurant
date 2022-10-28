# Demonstration of making classes

from one_moon_restaurant.classes import recipes
from one_moon_restaurant.classes.recipes import Recipe


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
    def __init__(self, title, cost, number_serves, instructions='', long_desc='', short_desc='', item_type='catering'):
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


def recipe_to_menu_item(recipe: Recipe, cost: int) -> MenuItem:
    menu_item = MenuItem(title=recipe.title,
                         cost=cost)
    short_desc = 'Ingredients: ' + ', '.join(str(x) for x in recipe.ingredients)
    long_desc = short_desc + '\n' + recipe.notes
    menu_item.change_description(long_desc=long_desc, short_desc=short_desc)
    return menu_item


# Defining the available items as classes
black_back_perch_stew = recipe_to_menu_item(recipe=recipes.black_back_perch_stew, cost=4500)
come_and_get_it = recipe_to_menu_item(recipe=recipes.come_and_get_it, cost=5000)
crystal_shrimp = recipe_to_menu_item(recipe=recipes.crystal_shrimp, cost=4500)
squirrel_fish = recipe_to_menu_item(recipe=recipes.squirrel_fish, cost=5000)
triple_layered_consomme = recipe_to_menu_item(recipe=recipes.triple_layered_consomme, cost=4500)
universal_peace = recipe_to_menu_item(recipe=recipes.universal_peace, cost=5000)


# Example of a Catering class
universal_peace_catering = CateringItem(title=universal_peace.title,
                                        cost=universal_peace.cost,
                                        number_serves=4,
                                        instructions='Chef Ganyu\'s special: Prosperous Peace',
                                        long_desc=universal_peace.long_desc,
                                        short_desc=universal_peace.short_desc,
                                        item_type=universal_peace.item_type)

# Setting up the menu
weekend_menu = Menu(breakfast=[universal_peace],
                    lunch=[squirrel_fish],
                    dinner=[come_and_get_it])

workday_menu = Menu(breakfast=[crystal_shrimp],
                    lunch=[triple_layered_consomme],
                    dinner=[black_back_perch_stew])

# Printing the menu to scrutinize everything
# workday_menu.print_menu()
# come_and_get_it.print_item(desc_type='long')
# universal_peace.print_item(desc_type='short')
