# One Moon Restaurant (README)

This repository is made as a demonstration of Python skills.
The files are made in accordance to examples and exercises present in Katie Cunningham's book "SamsTeachYourself Python in 24 Hours".
All examples and exercises from the books are expanded and improved in the repository.
For each chapter in the book denoted by "Hour", the repository is updated every week (tentatively).

The repository hosts .py scripts and code snippets related to managing a hypothetical restaurant named "One Moon Restaurant".
The food recipes and ingredients used for the codes are from Genshin Impact, not from the book.

## Changelog
Week 16 - Created classes/inventory.txt for demonstration of working with program files
        - Updated classes/ingredients.py with minor changes
        - Updated classes/inventory.py
            - Added sort() function for Inventory class
            - Updated add() function for Inventory class incorporating sort() function
            - Updated remove() and has() functions for Inventory class with minor changes
            - Added load_inventory_from_file() function to import inventory items from inventory.txt to codes
            - Added write_inventory_to_file() function to export inventory files from codes to inventory.txt

Week 15 - Created README.txt, INSTALL.txt
        - Updated all files to contain docstrings

## Files Included
- inventorycheck.py         : A program to check if a certain item is available in the inventory
- receipt.py                : A program to calculate the total bill of a table
- specials.py               : A program to check the special dishes for different lunchtimes on different days of the week
- test.py                   : A program to test different classes and functions to see if they work properly
- classes/ingredients.py    : Contains the Ingredients class and defines for the ingredients needed for inventories and recipes
- classes/inventory.py      : Contains the Inventory class, related functions and the changes in inventory of the restaurant
- classes/inventory.txt     : Contains a demo list of ingredients to use in inventory.py
- classes/items.py          : Contains the MenuItem, CateringItem and Menu classes, related functions and the item and menu defines
- classes/recipes.py        : Contains the Recipe class and defines all the recipes
- functions/input_handler.py: Contains the function for sanitizing the user's input

## Acknowledgement
All the examples and exercise problems are credited to Katie Cunningham and her book "SamsTeachYourself Python in 24 Hours".
The credits for the item names are due to Hoyoverse and their game Genshin Impact.

## Contact Information
For any inquiry, contact rahman.fahimur2109@gmail.com
