# Demonstration of splitting up a program

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
