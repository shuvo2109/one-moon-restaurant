# Demonstration of processing inputs and outputs
# Demonstration of using loops to repeat code
# Demonstration of using dictionaries to pair keys with values
from functions.input_handler import refine_input


def get_specials():
    # Defining the specials in each day
    sunday = {'B': 'Universal Peace\nIngredients: Berry, Carrot, Lotus Head, Rice',
              'L': 'Squirrel Fish\nIngredients: Fish, Flour, Sugar, Tomato',
              'D': 'Come and Get It\nIngredients: Fish, Raw Meat, Rice, Tofu'}
    monday = {'B': 'Crystal Shrimp\nIngredients: Carrot, Rice, Shrimp Meat',
              'L': 'Triple-Layered Consomme\nIngredients: Bamboo Shoot, Fowl, Ham',
              'D': 'Black-Back Perch Stew\nIngredients: Fish, Jueyun Chili, Salt'}

    # Saturday has the same specials. Mon - Fri has same specials.
    tuesday = monday
    wednesday = monday
    thursday = monday
    friday = monday
    saturday = sunday

    # Defining the days in special's dictionary
    specials = {'sun': sunday,
                'mon': monday,
                'tue': tuesday,
                'wed': wednesday,
                'thu': thursday,
                'fri': friday,
                'sat': saturday}

    return specials


def print_special(special):
    print("\nThe special is: {}".format(special))
    print("*"*15)


def get_day():
    weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    day = refine_input(prompt="\nEnter day of the week\n[sun / mon / tue / wed / thu / fri / sat]: ", type_=str, range_=weekdays)
    return day


def get_time():
    dine_times = ['B', 'L', 'D']
    time = refine_input(prompt="\nEnter the mealtime\n['B' for breakfast, 'L' for lunch, 'D' for dinner]: ", type_=str, range_=dine_times)
    return time


def main():
    # Defining the specials
    specials = get_specials()

    # Greetings
    print("Welcome to One Moon Restaurant\'s Specials Program!")
    print("*" * 20)

    # Specials check start
    while True:
        day = get_day()
        special = specials[day]
        time = get_time()
        print_special(special[time])

        # Termination
        end = input("\nDo you want to calculate another special?\n[\'n\' for no, \'y\' or anything else for yes]: ")
        if end.strip().lower() == 'n':
            end = input("\nHave a nice rest of the day.\nPress ENTER to close program.")
            break


if __name__ == "__main__":
    main()

# Original code for archive purpose
# Version 1
# # Defining the specials
# # Breakfast Special Dish
# breakfast_special = "Come and Get It"
# breakfast_notes = "A luxurious dish made out of Raw Meat, Fish, Rice and Tofu.\n"
#
# # Lunch Special Dish
# lunch_special = "Universal Peace"
# lunch_notes = "Colorful staple food with Rice, Lotus Head, Carrot and Berry.\n"
#
# # Dinner Special Dish
# dinner_special = "Squirrel Fish"
# dinner_notes = "A sophisticated Fish dish with Tomato, Flour and Sugar.\n"
#
#
#
# # Running loop for multiple entries
# while True:
#     # Input from the user
#     meal_time = input("Which mealtime do you want?\n[breakfast / lunch / dinner / 'q' to quit]: ")
#
#     # Check for quitting
#     if meal_time.strip().lower() == 'q':
#         break
#
#     # Output: special dish based on meal time
#     print("Specials for {}:".format(meal_time.strip().lower()))
#     if meal_time.strip().lower() == "breakfast":
#         print(breakfast_special)
#         print(breakfast_notes)
#     elif meal_time.strip().lower() == "lunch":
#         print(lunch_special)
#         print(lunch_notes)
#     elif meal_time.strip().lower() == "dinner":
#         print(dinner_special)
#         print(dinner_notes)
#     else:
#         print("Sorry, {} isn\'t valid.\n".format(meal_time.strip().lower()))
#
# # Farewell
# print("\nGoodbye!")
#
# # Termination
# end = input("Press ENTER to close program.")
#
# Version 2
# def print_invalid_input(input):
#     print("I am sorry but {} is not a valid input.\n".format(input))
#
#
# def get_specials():
#     # Defining the specials in each day
#     sunday = {'B': 'Universal Peace\nIngredients: Berry, Carrot, Lotus Head, Rice',
#               'L': 'Squirrel Fish\nIngredients: Fish, Flour, Sugar, Tomato',
#               'D': 'Come and Get It\nIngredients: Fish, Raw Meat, Rice, Tofu'}
#     monday = {'B': 'Crystal Shrimp\nIngredients: Carrot, Rice, Shrimp Meat',
#               'L': 'Triple-Layered Consomme\nIngredients: Bamboo Shoot, Fowl, Ham',
#               'D': 'Black-Back Perch Stew\nIngredients: Fish, Jueyun Chili, Salt'}
#
#     # Saturday has the same specials. Mon - Fri has same specials.
#     tuesday = monday
#     wednesday = monday
#     thursday = monday
#     friday = monday
#     saturday = sunday
#
#     # Defining the days in special's dictionary
#     specials = {'sun': sunday,
#                 'mon': monday,
#                 'tue': tuesday,
#                 'wed': wednesday,
#                 'thu': thursday,
#                 'fri': friday,
#                 'sat': saturday}
#
#     return specials
#
#
# def print_special(special):
#     print("\nThe special is: {}".format(special))
#     print("*"*15)
#
#
# def get_day():
#     weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
#     while True:
#         day = input("\nEnter day of the week\n[Sun / Mon / Tue / Wed / Thu / Fri / Sat]: ")
#         if day[0:3].lower() in weekdays:
#             return day[0:3].lower()
#         else:
#             print_invalid_input(day)
#
#
# def get_time():
#     dine_times = ['B', 'L', 'D']
#     while True:
#         time = input("\nEnter the mealtime\n['B' for breakfast, 'L' for lunch, 'D' for dinner]: ")
#         if time[0].upper() in dine_times:
#             return time[0].upper()
#         else:
#             print_invalid_input(time)
#
#
# def main():
#     # Defining the specials
#     specials = get_specials()
#
#     # Greetings
#     print("Welcome to One Moon Restaurant\'s Specials Program!")
#     print("*" * 20)
#
#     # Specials check start
#     while True:
#         day = get_day()
#         special = specials[day]
#         time = get_time()
#         print_special(special[time])
#
#         # Termination
#         end = input("\nDo you want to calculate another special?\n[\'n\' for no, \'y\' or anything else for yes]: ")
#         if end.strip().lower() == 'n':
#             end = input("\nHave a nice rest of the day.\nPress ENTER to close program.")
#             break
#
#
# if __name__ == "__main__":
#     main()