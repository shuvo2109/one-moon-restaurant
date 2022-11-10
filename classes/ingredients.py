# Demonstration of splitting up a program

class Ingredient(object):
    """ Class for ingredients, used in defining inventory and recipes.
    """
    def __init__(self, title, description=''):
        """ Sets up an Ingredient.
            Requires a title and a description.
            Both has to be strings.
            Title is mandatory but description is optional.
        """
        self.title = title
        self.description = description

    def __str__(self):
        """ Returns the title of the Ingredient.
        """
        return self.title


# Inventory ingredients
bamboo_shoot = Ingredient(title='Bamboo Shoot')
carrot = Ingredient(title='Carrot')
crab = Ingredient(title='Crab')
fish = Ingredient(title='Fish')
flour = Ingredient(title='Flour')
ham = Ingredient(title='Ham')
jueyun_chili = Ingredient(title='Jueyun Chili')
lotus_head = Ingredient(title='Lotus Head')
matsutake = Ingredient(title='Matsutake')
mushroom = Ingredient(title='Mushroom')
radish = Ingredient(title='Radish')
sausage = Ingredient(title='Sausage')
sugar = Ingredient(title='Sugar')

# Recipe ingredients
berry = Ingredient(title='Berry')
fowl = Ingredient(title='Fowl')
raw_meat = Ingredient(title='Raw Meat')
rice = Ingredient(title='Rice')
salt = Ingredient(title='Salt')
shrimp_meat = Ingredient(title='Shrimp Meat')
tofu = Ingredient(title='Tofu')
tomato = Ingredient(title='Tomato')
