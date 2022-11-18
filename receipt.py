# Demonstration of using loops to repeat code
# Demonstration of using functions to create reusable codes
# Demonstration of using Python's modules to add functionality

import json
import os
from datetime import datetime
from functions.input_handler import refine_input, str_rjust


def get_seat_total(seat: list) -> float:
    """ Calculates the total bill for a seat.
        Input has to be a List with the cost of each item consumed as elements of the List.
    """
    total = 0
    for item in seat:
        total = total + item
    return total


def print_seat(seat: list):
    """ Prints the total bill for a seat, item by item and sum.
        Input has to be a List with the cost of each item consumed as elements of the List.
    """
    for i in range(0, len(seat)):
        item = seat[i]
        print("Item {}: ${}".format(i+1, round(item, 2)))
    print("-"*15)
    total = get_seat_total(seat)
    print("Total: ${}\n".format(round(total, 2)))


def load_receipt_from_file(filename: str) -> dict:
    """ Opens a receipt file from the receipts/ directory with the filename provided.
    """
    try:
        f = open('receipts/' + filename)
        receipts = json.load(f)
        f.close()
    except OSError:
        print("Could not locate file. Creating empty receipt.")
        receipts = {}
    return receipts


def write_receipt_to_file(grand_total: float):
    """ Saves the grand total of a bill to a .json file
    """
    try:
        os.mkdir('receipts')
    except OSError:
        print("Failed to make directory.")
        pass

    # Load date and time for file and key creation
    date = datetime.now()
    filename = str_rjust(date.year) + str_rjust(date.month) + str_rjust(date.day) + '.json'
    receipts = load_receipt_from_file(filename=filename)
    key = str_rjust(date.hour) + str_rjust(date.minute) + str_rjust(date.second)

    # Store grand_total
    receipts[key] = grand_total

    # Open file, dump json data and close
    f = open('receipts/' + filename, 'w')
    json.dump(receipts, f, indent=2)
    f.close()


def original_receipt_program():
    # Bill calculation start
    while True:
        # Loop initialization
        seats = [[]]
        seat = 0
        item = 0
        bill = 0

        # Loop to take bill inputs
        while True:
            while True:
                # Input
                bill = input("\nEnter the bill for Seat {}, Item {}.\n[\'n\' for the next seat, \'q\' to end input]: "
                             .format(seat + 1, item + 1))

                # Check for next seat input
                if bill.strip().lower() == 'n':
                    break

                # Check for quitting
                if bill.strip().lower() == 'q':
                    break

                # Input Cleaning
                try:
                    bill = round(float(bill.strip()), 2)
                except ValueError:
                    print("Sorry, that is not a valid input.")
                    continue

                # Add bill to the seat
                seats[seat].append(bill)

                # Update to receive next item's input
                item = item + 1

            # Check for quitting
            if bill.strip().lower() == 'q':
                break

            # Update to receive next seat's input
            seats.append([])
            seat = seat + 1
            item = 0

        # Seat-wise bill output
        grand_total = 0
        grand_total_tipped = 0
        for i in range(0, len(seats)):
            seat = seats[i]
            print("\nSeat No. {}".format(i + 1))
            print_seat(seat)
            grand_total = grand_total + get_seat_total(seat)

        print("=" * 15)

        # Tipping policy
        if len(seats) > 8:
            grand_total_tipped = grand_total * 1.03
            print("Since the party size was bigger than eight, a 3% tips has been automatically added.\n")

            # Grand total output:
            print("Grand total (w/o tips):  ${}\nGrand total (with tips): ${}"
                  .format(round(grand_total, 2), round(grand_total_tipped, 2)))
        else:
            # Grand total output
            print("Grand total: ${}".format(round(grand_total, 2)))

        # Date and time printing
        time = datetime.now()
        print("Receipt printing time: {D}-{M}-{Y} {HR}:{MIN}"
              .format(D=time.day, M=time.month, Y=time.year, HR=time.hour, MIN=time.minute))

        # Saving grand total to a .json file for the day
        write_receipt_to_file(max(grand_total, grand_total_tipped))

        # Termination
        end = input("\nDo you want to calculate another receipt?\n[\'n\' for no, \'y\' or anything else for yes]: ")
        if end.strip().lower() == 'n':
            end = input("\nHave a nice rest of the day.\nPress ENTER to close program.")
            break


def daily_grand_total_calculator():
    while True:
        # Input
        filename = input("Enter the JSON file name: ")

        # Correcting for file extension
        if filename[-5:] != '.json':
            filename = filename + '.json'

        # Load JSON file with the bill
        receipts = load_receipt_from_file(filename=filename)

        # Total daily bill calculation
        daily_total = 0
        for bill in receipts:
            daily_total += receipts[bill]

        print("\nTotal daily bill for {file} is ${amount}".format(file=filename[:-5], amount=daily_total))

        # Termination
        end = input("\nDo you want to calculate another daily grand total?\n[\'n\' for no, \'y\' or anything else for yes]: ")
        if end.strip().lower() == 'n':
            end = input("\nHave a nice rest of the day.\nPress ENTER to close program.")
            break


def main():
    # Greetings
    print("Welcome to One Moon Restaurant\'s Receipt Program!")
    print("*" * 20)

    # Getting user's opinion about what they want to do
    options = [1, 2]
    prompt = "\nWhat would you like to do?\n" \
             "Enter 1 to calculate the total bill of a table.\n" \
             "Enter 2 to calculate the grand total earning of a day: "

    choice = refine_input(prompt=prompt, type_=int, range_=options)

    if choice == 1:
        original_receipt_program()
    elif choice == 2:
        daily_grand_total_calculator()


if __name__ == "__main__":
    main()
