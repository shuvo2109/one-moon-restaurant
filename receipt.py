# Demonstration of using loops to repeat code
# Demonstration of using functions to create reusable codes
# Demonstration of using Python's modules to add functionality

from datetime import datetime


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


def main():
    # Greetings
    print("Welcome to One Moon Restaurant\'s Receipt Program!")
    print("*" * 20)

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
        for i in range(0, len(seats)):
            seat = seats[i]
            print("\nSeat No. {}".format(i+1))
            print_seat(seat)
            grand_total = grand_total + get_seat_total(seat)

        print("="*15)

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

        # Termination
        end = input("\nDo you want to calculate another receipt?\n[\'n\' for no, \'y\' or anything else for yes]: ")
        if end.strip().lower() == 'n':
            end = input("\nHave a nice rest of the day.\nPress ENTER to close program.")
            break


if __name__ == "__main__":
    main()
