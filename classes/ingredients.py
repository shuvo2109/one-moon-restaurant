# Demonstration of splitting up a program

class Ingredient(object):
    def __init__(self, title, description=''):
        self.title = title
        self.description = description

    def __str__(self):
        return self.title
