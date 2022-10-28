# Demonstration of splitting up a program

from one_moon_restaurant.classes import ingredients


class Recipe(object):
    def __init__(self, title, ingredients=[], notes=''):
        self.title = title
        self.ingredients = ingredients
        self.notes = notes

    def __str__(self):
        return self.title

    def print_recipe(self):
        print(self.title)
        print("Ingredients:")
        for item in self.ingredients:
            print(item)
        if self.notes:
            print("Special Notes:")
            print(self.notes)


# Ingredients define
black_back_perch_stew_ingredients = [ingredients.fish,
                                     ingredients.jueyun_chili,
                                     ingredients.salt]

come_and_get_it_ingredients = [ingredients.fish,
                               ingredients.raw_meat,
                               ingredients.rice,
                               ingredients.tofu]

crystal_shrimp_ingredients = [ingredients.carrot,
                              ingredients.rice,
                              ingredients.shrimp_meat]

triple_layered_consomme_ingredients = [ingredients.bamboo_shoot,
                                       ingredients.fowl,
                                       ingredients.ham]

squirrel_fish_ingredients = [ingredients.fish,
                             ingredients.flour,
                             ingredients.sugar,
                             ingredients.tomato]

universal_peace_ingredients = [ingredients.berry,
                               ingredients.carrot,
                               ingredients.lotus_head,
                               ingredients.rice]

# Recipes
black_back_perch_stew = Recipe(title='Black-back Perch Stew',
                               ingredients=black_back_perch_stew_ingredients,
                               notes='Xiangling\'s special: Wanmin Restaurant\'s Boiled Fish')

come_and_get_it = Recipe(title='Come and Get It',
                         ingredients=come_and_get_it_ingredients,
                         notes='Qiqi\'s special: No Tomorrow')

crystal_shrimp = Recipe(title='Crystal Shrimp',
                        ingredients=crystal_shrimp_ingredients,
                        notes='Xingqiu\'s special: All-Delicacy Parcels')

triple_layered_consomme = Recipe(title='Triple-layered Consomme',
                                 ingredients=triple_layered_consomme_ingredients)

squirrel_fish = Recipe(title='Squirrel Fish',
                       ingredients=squirrel_fish_ingredients)

universal_peace = Recipe(title='Universal Peace',
                         ingredients=universal_peace_ingredients,
                         notes='Ganyu\'s special: Prosperous Peace')
