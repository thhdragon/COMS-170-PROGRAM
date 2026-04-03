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
# file_path         Path                  path to the file
# file              file                  file object
# err               Exception             exception object
# --------------------------------------------------------------------------------
from pathlib import Path


# CalcTotal function takes no arguments and returns two floats or None on failure
def CalcTotal() -> tuple[float, float] | None:
    """Calculate grand total and average sale amount. Returns tuple on success, None on failure."""
    # initialize prices to 0.0 and idx to 0
    prices: float = 0.0
    idx: int = 0
    # use Path from pathlib to get a handle to the file path (preferred method in official docs)
    file_path = Path("cards.txt")
    # opening a file can fail so use a try block
    try:
        # official docs recommend opening files with `with`
        # `with` makes sure `file` is closed automatically and cleans up on errors
        # use the path handle to get a file handle by using the open method on file_path
        # only need to read so open in read mode with "r"
        with file_path.open("r") as file:
            # the built in iterator for file objects reads one line at a time
            # so iterating through `file` reads one line at a time
            # use a for loop to iterate through the file
            for line in file:
                # strip whitespace from the current line and store in line_cleaned
                line_cleaned: str = line.strip()
                # I don't know if I should be expecting you to mess with the cards.txt
                # use try block to convert the cleaned line to a float (can fail)
                # if blank line
                if not line_cleaned:
                    # if the line is blank, skip to the next iteration
                    continue
                try:
                    # cast cleaned line to float and store in price
                    price: float = float(line_cleaned)
                except ValueError:
                    print(f"'{line_cleaned}' is not a valid number.")
                    continue
                # increment the number of cards read from the file by +1 each iteration
                idx += 1
                # add the price to the accumulated total
                prices += price

    # FileNotFoundError is raised if the file is not found
    except FileNotFoundError as err:
        # print the error message and a hint to fix it
        # file is probably not in working directory
        print(f"{err}: Make sure the file is in the current working directory.")
        # return None
        return None

    # calculate the average. (can fail if idx is 0)
    # if the file is empty the index variable will never increment from 0
    # can fail so use a try block
    try:
        # attempt to calculate average
        average: float = prices / idx
    # if idx is 0 catch the ZeroDivisionError and return None for main to use
    except ZeroDivisionError:
        print("Error: This should only happen if the file is empty. Check cards.txt.")
        return None

    # return the total and average
    return prices, average


# DisplayCardSales function takes no arguments and returns None
def DisplayCardSales() -> None:
    """Display scores for all items in the text file provided. Can fail."""
    # reuses a lot from CalcTotal so I'll go lighter on the comments.
    # initialize idx
    idx: int = 0
    # get a handle to the file path
    file_path = Path("cards.txt")
    # try block to catch file not found
    try:
        # open the file. call it file.
        with file_path.open("r") as file:
            # read through the file line by line with a for loop
            for line in file:
                # strip whitespace from the current line and store in line_cleaned
                line_cleaned: str = line.strip()
                # use try block to convert the cleaned line to a float (can fail)
                try:
                    # cast cleaned line to float and store in price
                    price: float = float(line_cleaned)
                # if the line isn't a valid number or is blank, print an error and skip to the next line
                except ValueError:
                    print(f"'{line_cleaned}' is not a valid number.")
                    continue
                # increment the number of cards read from the file by +1 each iteration
                idx += 1
                # print the line number and the price
                print(f"{idx}: ${price:.2f}")

    # FileNotFoundError is raised if the file is not found
    except FileNotFoundError as err:
        # print the error message and a hint to fix it
        # file is probably not in working directory
        print(f"{err}: Make sure the file is in the current working directory.")
        # return early from the function
        return


def main() -> None:
    """Display a menu of choices to the user.

    Menu choices are:
    C: Calculate Total and Average Sales
    D: Display Sales
    X: Exit

    The menu is displayed until the user enters 'x' to exit the application.
    """
    # initialize menu_selection
    menu_selection: str = ""
    # loop until the user enters 'x'
    while menu_selection != "x":
        # print the menu
        print(
            f"{'-' * 28}\n*   Pokemon Card Sales   *\n{'-' * 28}\n"
            "C: Calculate Total and Average Sales\nD: Display Sales\nX: Exit\n",
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
                # print the error message and a hint to fix it
                print("Try after addressing above errors")
                # continue to the next iteration
                continue
            # response has two values inside. unpack into total and average
            total, average = response
            # print the total and average formatted to 2 decimal places
            print(f"Total Sales: ${total:.2f}\nAverage Sale: ${average:.2f}")

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
# on functions like float | None, which is a lot nicer than using Optional[float] from the typing
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
