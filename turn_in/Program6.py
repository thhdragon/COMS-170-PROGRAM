# Tyler Hill
# 0506760
# Program 6
# COMS-170-01: Winter 2026
# Due: 04/03/26
# Program description: displays the card sale prices from a text file to screen
# and calculates the average sale amount
# --------------------------------------------------------------------------------
# Variable          Type                  Purpose
# --------------------------------------------------------------------------------
# price             float                 holds the price of a card read from the file
# prices            float                 holds the total price of all cards read from the file
# idx               int                   holds the number of cards read from the file
# menu_selection    str                   holds the user's menu selection
# total             float                 holds the total price of all cards read from the file
# average           float                 holds the average price of all cards read from the file
# line_cleaned      str                   holds the cleaned line read from the file, with whitespace removed
# response          tuple[float, float]   holds the total and average prices
# file              file                  holds the file object
# err               Exception             holds the exception object
# --------------------------------------------------------------------------------
from pathlib import Path

# CalcTotal function takes no arguments and returns two floats or None on error
def CalcTotal() -> tuple[float, float] | None:
    """Calculate grand total and average sale amount.

    Reads the text file provided ('cards.txt'), accumulates a total,
    and divides the total by the number of items in the file.

    Returns:
        grand total and the average sales amount, or None if an error occurs.

    """
    # initialize variables prices and idx
    prices: float = 0.0
    idx: int = 0
    # opening a file can fail so use a try block
    try:
        # use Path from pathlib to open the file (preferred method in official docs)
        # official docs recommend opening files with `with`
        # `with` ensures `file` is closed automatically and cleans up on errors
        with Path("cards.txt").open("r") as file:
            # the iterator protocol on file objects reads one line at a time
            # so iterating through `file` reads one line at a time
            # use a for loop to iterate through the file
            for line in file:
                # use .strip() to remove whitespace from the line
                line_cleaned: str = line.strip()
                # I don't know if I should be expecting you to mess with the cards.txt
                # add a check to make sure there isn't a blank line in the file
                # python EAFP isnt really my style so LBYL
                if not line_cleaned:
                    # if so continue to the next line
                    continue
                # convert the cleaned line to a float
                # this isn't a simple test because isdigit() doesn't work for floats
                # cast the cleaned line to a float and rely on the try block to catch errors
                price: float = float(line_cleaned)
                # increment the number of cards read from the file by +1 each iteration
                idx += 1
                # add the price to the total
                # shorthand for `prices = prices + price`
                prices += price

    # blocks to jump to if an error occurs
    # FileNotFoundError is raised if the file is not found
    except FileNotFoundError as err:
        # print the error
        print(err)
        # return None
        return None
    # ValueError is raised if the line entry is not a float
    except ValueError as err:
        # print the error
        print(f"Error, check your file contents.\n{err}")
        # return None
        return None

    # catch ZeroDivisionError with LBYL look before you leap
    # if idx is 0, the file is empty
    if idx == 0:
        # print the error
        print("The file is empty. Please add data to 'cards.txt'.")
        # return None
        return None

    # calculate the average
    average: float = prices / idx
    # return the total and average
    return prices, average


def DisplayCardSales() -> None:
    """Display scores for all items in the text file provided.

    Reads from a text file ('cards.txt') and displays each score with a
    line number to the left starting at 1. Also handles file and value errors.
    """
    # sounded like you wanted this done manually instead of using enumerate() on a list
    # initialize idx
    idx: int = 0
    # opening a file can fail so use a try block
    try:
        # use with to open the file
        with Path("cards.txt").open("r") as file:
            # iterate through the file by lines
            for line in file:
                # clean the line
                line_cleaned: str = line.strip()
                # again lets LBYL look before you leap
                # if the line is not empty
                if not line_cleaned:
                    # continue to the next line
                    continue
                # convert the cleaned line to a float
                price: float = float(line_cleaned)
                # increment the number of cards read from the file by +1 each iteration
                idx += 1
                # print the line number and the price
                print(f"{idx}: ${price:.2f}")

    # blocks to jump to if an error occurs
    # FileNotFoundError is raised if the file is not found
    except FileNotFoundError as err:
        # print the error
        print(f"{err}: Ensure file is in the current working directory.")
        # return None
        return
    # ValueError is raised if the line entry is not a float
    except ValueError as err:
        print(f"Error, check your file contents.\n{err}")
        return


def main() -> None:
    """Display a menu of choices to the user.

    Menu choices are:
    D: Display Sales
    C: Calculate Total and Average
    X: Exit application

    The menu is displayed until the user enters 'x' to exit the application.
    """
    # initialize menu_selection
    menu_selection: str = ""
    # loop until the user enters 'x'
    while menu_selection != "x":
        # print the menu
        print(
            "**********************\n* Pokemon Card Sales *\n**********************\n"
            "D: Display Sales\nC: Calculate Total and Average\nX: Exit application\n",
        )
        # get user input and convert to lowercase so I don't have to check for both cases
        menu_selection = input("Enter menu selection: ").lower()

        # check if the menu selection is valid by checking if it's in C D X
        if menu_selection not in ("c", "d", "x"):
            # print the error
            print(f"Pick a valid menu option. '{menu_selection.upper()}' is not an option")
            # continue to the next iteration
            continue

        # if the menu selection is C
        if menu_selection == "c":
            # call the CalcTotal function
            response: tuple[float, float] | None = CalcTotal()
            # if the response is None
            if response is None:
                # print the error
                print("Try after addressing above errors")
                # continue to the next iteration
                continue
            # unpack response into total and average
            total, average = response
            # print the total and average
            print(f"Total Sales: ${total:.2f}\nAverage Sale:  ${average:.2f}")

        # if the menu selection is D
        elif menu_selection == "d":
            # call the DisplayCardSales function
            DisplayCardSales()


main()
# =========Comments/Explanation of code from outside the lectures=========
