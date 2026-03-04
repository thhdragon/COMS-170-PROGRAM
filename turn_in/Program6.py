# Tyler Hill
# 0506760
# Program 6
# COMS-170-01: Winter 2026
# Due: 04/03/26
# Program description: program displays the card sale prices to screen
# calculate the average sale amount
# --------------------------------------------------------------------------------
# Variable          Type          Purpose
# --------------------------------------------------------------------------------
# price             float         holds the price of a card read from the file
# prices            float         holds the total price of all cards read from the file
# idx               int           holds the number of cards read from the file
# menu_selection    str           holds the user's menu selection
# total             float         holds the total price of all cards read from the file
# average           float         holds the average price of all cards read from the file
# line_cleaned      str           holds the cleaned line read from the file, with trailing whitespace removed
# --------------------------------------------------------------------------------
from pathlib import Path


def CalcTotal() -> tuple[float, float] | None:
    """Calculate grand total and average sale amount.

    Reads the text file provided ('cards.txt'), accumulates a total,
    and divides the total by the number of items in the file.

    Returns:
        A tuple containing the grand total and the average sales amount, or None if an error occurs.

    """
    prices = 0.0
    idx = 0
    try:
        with Path("cards.txt").open("r") as file:
            for line in file:
                line_cleaned = line.rstrip()
                price = float(line_cleaned)
                idx += 1
                prices += price

    except FileNotFoundError as err:
        print(err)
        return None
    except ValueError as err:
        print(f"Error, check your file contents.\n{err}")
        return None

    return prices, (prices / idx)


def DisplayCardSales() -> None:
    """Display scores for all items in the text file provided.

    Reads from a text file ('cards.txt') and displays each score with a
    line number to the left starting at 1. Also handles file and value errors.
    """
    # sounded like you wanted this done manually instead of using enumerate() on a list
    idx = 0
    try:
        with Path("cards.txt").open("r") as file:
            for line in file:
                line_cleaned = line.rstrip()
                price = float(line_cleaned)
                idx += 1
                print(f"{idx}: ${price:.2f}")

    except FileNotFoundError as err:
        print(err)
        return
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
    menu_selection = ""
    while menu_selection != "x":
        print(
            "**********************\n* Pokemon Card Sales *\n**********************\n"
            "D: Display Sales\nC: Calculate Total and Average\nX: Exit application\n",
        )
        menu_selection = input("Enter menu selection: ").lower()

        if menu_selection not in ("c", "d", "x"):
            print(f"Pick a valid menu option. {menu_selection.upper()} is not an option")
            continue

        if menu_selection == "c":
            response: tuple[float, float] | None = CalcTotal()
            if response is None:
                print("Try after addressing above errors")
                continue
            total, average = response
            print(f"Total Sales: ${total:.2f}\nAverage Sale:  ${average:.2f}")

        elif menu_selection == "d":
            DisplayCardSales()


main()
# =========Comments/Explanation of code from outside the lectures=========
