# Demonstration of splitting up a program

from classes.ingredients import Ingredient
from classes.recipes import Recipe


def main():
    # A test to see if the classes work as intended
    i = Ingredient(title="Bird Egg")
    r = Recipe(title="Teyvat Fried Egg", ingredients=[i])

    r.print_recipe()


if __name__ == "__main__":
    main()
