# Tyler Hill
# 0506760
# Program 5
# COMS-170-01: Winter 2026
# Due: 03/20/26
# Program description: Program prompts user for account interest values
# and calculates the total interest earned and the total account value.
# ----------------------------------------------------------------------------
# Variable       Type        Purpose
# ----------------------------------------------------------------------------
# principal      float       amount of money to invest. user input
# rate           float       interest rate % as a whole number. user input
# years          int         number of years to invest. user input
# interest       float       amount of interest earned. calculated
# total_account  float       total amount of money in the account. calculated
# menu_choice    str         user input for menu choices
# ----------------------------------------------------------------------------


def CalcInterest(principal: float, rate: float, time: int) -> float:
    """Calculate interest from user input.

    Calculates interest by multiplying the principal, rate, and time.
    (interest = principal * rate * time)

    Args:
        principal: initial amount of money used to calculate interest.
        rate: annual interest rate in percentage.
        time: number of years used to calculate interest.

    Returns:
        Amount of interest earned. return is divided by 100 to convert from percentage to decimal

    """
    # could easily just return the calculation directly but I'm trying to write this in the most
    # self documenting way so added an intermediate variable
    interest: float = (principal * rate * time) / 100
    return interest


def TotalAccount() -> tuple[float, float]:
    """Prompt user for input sends to CalcInterest.

    Prompts user for principal, rate, and time. Then passes values to CalcInterest.
    Input() strings are cast to integers and the input is assumed to be valid.

    Returns:
        The interest earned and the total account value.
        The first value is the interest earned and the second value is the total account value.

    """
    print(
        "\nEnter the interest rate entered as a percentage, "
        "(e.g., enter 6 for 6% interest)\n"
        "and the number of years the money will be invested.\n",
    )

    # casting an input() string to int will fail with ValueError if the string isn't valid numbers.
    # this should go into a try/except block but KISS for now. Exceptions are next unit.
    # also assuming that principal is an int not a float based on the test cases in the program pdf.
    principal = float(input("Enter the amount of money (principal) you will be investing: $"))
    rate = float(input("Enter the annual interest rate (a value of 5 = 5% annual interest): "))
    years = int(input("Enter the whole number of years you will be investing: "))

    # calculate interest by passing principal, rate, and years to CalcInterest() and storing the
    # result in interest
    interest: float = CalcInterest(
        principal,
        rate,
        years,
    )

    # add interest to principal to get total
    total_account: float = principal + interest

    # return the interest and total account value
    return interest, total_account


def DisplayInfo() -> None:
    """Provide information about the interest formula."""
    print(
        "\nThe simple interest formula is: Interest = Principal x Rate x Time\n"
        "The Principal is the amount of money invested.\n"
        "The Rate is the annual interest rate the money will earn.\n"
        "The Time is the number of years the money will be invested for.\n",
    )


def main() -> None:
    """Display menu and handle user input."""
    # initialize menu_choice to an empty string so the while loop runs at least once
    menu_choice = ""
    # loop until user enters x
    while menu_choice != "x":
        # print menu intro message
        print("**  Interest Value Calculator  **")
        # get user input for menu choice
        # cast it to lower so we dont have to compare both cases
        msg = "C: Calculate Interest\nD: Display Interest Information\nX: Exit application\nUser Input: "
        menu_choice: str = input(msg).lower()
        if menu_choice in ("c", "d", "x"):  # validate input against menu options
            # match would be cleaner here but we haven't covered it yet and its only python 3.10+ anyways
            if menu_choice == "c":  # if menu_choice is "c"
                # call TotalAccount(), store results into interest and total
                interest, total = TotalAccount()

                # print the interest and total account value with formatting to 2 decimal places
                print(
                    f"\nTotal Interest Earned: ${interest:.2f}\n"
                    f"Total Account Value:   ${total:.2f}\n",
                )

            # if menu_choice is "d"
            elif menu_choice == "d":
                # display information by calling DisplayInfo()
                DisplayInfo()

            # if menu_choice is "x"
            elif menu_choice == "x":
                # print quit message
                print("\nHAL 9000: Daisy..Daisy..give me your answer do...")

        # if menu_choice is not "c", "d", or "x"
        else:
            # print error message
            # would probably put a continue here if there were more code under it
            print(f"Pick a valid menu option. '{menu_choice.upper()}' is not an option")


main()

# =========Comments/Explanation of code from outside the lectures=========
# I was using the program reqs from the assignment PDF as as comments to
# document the functions but they were basically everything that goes into a
# docstring so I figured why not just practice putting the information in actual
# docstrings instead of comments. I used the google style guide for python for
# the docstrings.
# https://google.github.io/styleguide/pyguide.html#383-functions-and-methods

# -------------Output as comments-----------------
# = RESTART: /home/tyler/Documents/MCC/COMS-170-PROGRAM/turn_in/Program5.py
# **  Interest Value Calculator  **
# C: Calculate Interest
# D: Display Interest Information
# X: Exit application
# User Input: c

# Enter the interest rate entered as a percentage, (e.g., enter 6 for 6% interest)
# and the number of years the money will be invested.

# Enter the amount of money (principal) you will be investing: $4200
# Enter the annual interest rate (a value of 5 = 5% annual interest): 4
# Enter the whole number of years you will be investing: 42

# Total Interest Earned: $7056.00
# Total Account Value:   $11256.00

# **  Interest Value Calculator  **
# C: Calculate Interest
# D: Display Interest Information
# X: Exit application
# User Input: d

# The simple interest formula is: Interest = Principal x Rate x Time
# The Principal is the amount of money invested.
# The Rate is the annual interest rate the money will earn.
# The Time is the number of years the money will be invested for.

# **  Interest Value Calculator  **
# C: Calculate Interest
# D: Display Interest Information
# X: Exit application
# User Input: x

# HAL 9000: Daisy..Daisy..give me your answer do...
