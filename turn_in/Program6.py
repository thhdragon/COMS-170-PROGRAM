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
# price             float                 price of a card read from the file
# prices            float                 total price of all cards read from the file
# idx               int                   number of cards read from the file
# menu_selection    str                   user's menu selection
# total             float                 total price of all cards read from the file
# average           float                 average price of all cards read from the file
# line_cleaned      str                   cleaned line read from the file with whitespace removed
# response          tuple[float, float]   total and average prices
# file              file                  file object
# err               Exception             exception object
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
    # if the file is empty the index variable will never increment from 0
    # thats a big problem because prices / idx will crash if idx is 0.
    # if idx is 0, the file is empty. 0 is a "falsy" value in python for an int
    # so check if idx is false aka empty
    if not idx:
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
    line number to the left starting at 1. Handles file and value errors.
    """
    # initialize idx
    idx: int = 0
    # opening a file can fail so use a try block
    try:
        # use with to open the file
        with Path("cards.txt").open("r") as file:
            # iterate through the file by lines
            # sounded like you wanted this done manually instead of using enumerate() on a list
            for line in file:
                # clean the line
                line_cleaned: str = line.strip()
                # check again
                # if the line is not empty
                if not line_cleaned:
                    # continue to the next line in the file
                    continue
                # convert the cleaned line to a float
                price: float = float(line_cleaned)
                # increment the number of cards read from the file by +1 each iteration
                idx += 1
                # print the line number and the price
                print(f"{idx}: ${price:.2f}")

    # blocks to jump to if an error occurs. None is used for orchestration in main
    # FileNotFoundError is raised if the file is not found
    except FileNotFoundError as err:
        # print the error
        print(f"{err}: Make sure the file is in the current working directory.")
        # return None
        return
    # ValueError is raised if the line entry is not a float
    except ValueError as err:
        # print the error
        print(f"Error, check your file contents.\n{err}")
        # return None
        return


def main() -> None:
    """Display a menu of choices to the user.

    Menu choices are:
    C: Calculate Total and Average
    D: Display Sales
    X: Exit application

    The menu is displayed until the user enters 'x' to exit the application.
    """
    # initialize menu_selection
    menu_selection: str = ""
    # loop until the user enters 'x'
    while menu_selection != "x":
        # print the menu
        print(
            f"{'-' * 28}\n*    Pokemon Card Sales    *\n{'-' * 28}\n"
            "C: Calculate Total and Average\nD: Display Sales\nX: Exit application\n",
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
            # print the total and average formatted to 2 decimal places
            print(f"Total Sales: ${total:.2f}\nAverage Sale:  ${average:.2f}")

        # if the menu selection is D
        elif menu_selection == "d":
            # call the DisplayCardSales function
            DisplayCardSales()


main()
# =========Comments/Explanation of code from outside the lectures=========
# I do a lot of independent learning and as I commented above I used a few of the more modern
# patterns for handling files and . This week added the requirement of handling errors in our
# programs so I read through the official Python docs which went over getting a handle to the
# exception object in the except block and printing it to get more information about the error.
# I'm used to using Err(e) in rust to get a handle (e) to the error message so the concept wasn't
# new and the syntax was easy just using the `as` keyword to set an alias.
# The docs on files also recommend pathlib and using `with` to open files in modern Python.
# Python 3.10+ stuff I'm not all that concerned about unless a pretty nice QoL like the union type
# on functions like Float | None, which is a lot nicer than using Optional[Float] from the typing
# module. But if it's a modern expected standard that's 10 years old now (3.4ish) it's a pattern I
# want to learn and use and I don't mind the extra work.
# I wasn't sure how defensive to be because I didn't want to go too far ahead of where we are in
# class but I was also concerned about losing points. I assume you aren't going to change the
# cards.txt contents but I made a wrong assumption last assignment and lost points so this might be
# a little overboard. I added a guard in the loops to skip blank lines in the cards.txt file and not
# throw an ValueError exception from trying to cast "" to float. I know erroring on a blank line in
# the file wouldn't have been "wrong" but silently skipping a blank line in the file seemed like the
# right way to handle it because if there are more lines (the for loop is still iterating), a blank
# line isn't a reason to crash a function like this. I also added a guard to make sure the file
# isn't empty because that would cause a ZeroDivisionError.
# I understand the significance of showing opening the file "manually" by getting a handle to open
# and then remembering to close it manually because like in C there is no `with`, its just fopen()
# and making sure to fclose().
# The None patterns I used are something I'm used to from rust because it's not far off from using
# Option<T>.
#
# It didn't specify whether the program needed to be defensive against a file with different
# contents but the post about error handling made it sound like it needed to be prepared for
# anything. I hit all the scenario I can think of except using a dynamic path for the file.
# Currently the program requires the cards.txt to be in the same directory as the current working
# directory of the terminal. The code snippet that I saw to handle automatically loading the
# cards.txt from same directory as the .py file looked like python magic I don't understand so I
# don't think it's something that was expected in this program. Google search showed a snippet like
# Get the directory where the script is located
# script_dir = Path(__file__).resolve().parent
# Build the path to your file
# file_path = script_dir / "data.txt"
