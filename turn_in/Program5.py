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
# principal      int         amount of money to invest. user input
# rate           int         interest rate % as a whole number. user input
# years          int         number of years to invest. user input
# interest       float       amount of interest earned. calculated
# total_account  float       total amount of money in the account. calculated
# menu_choice    str         user input for menu choice
# ----------------------------------------------------------------------------


def CalcInterest(principal: int, rate: int, years: int) -> float:
    """Calculate interest from user input.

    Calculates interest by multiplying the principal, rate, and time.
    (interest = principal * rate * time)

    Args:
        principal: initial amount of money used to calculate interest.
        rate: annual interest rate in percentage.
        years: number of years used to calculate interest. called years to not shadow time module.

    Returns:
        Amount of interest earned. return is divided by 100 to convert from percentage to decimal

    """
    return (principal * rate * years) / 100


def TotalAccount() -> tuple[float, float]:
    """Prompt user for input sends to CalcInterest.

    Prompts user for principal, rate, and years. Then passes values to CalcInterest.
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

    # casting an input() string to int can fail with ValueError if the string isn't valid numbers.
    # this should go into a try/except block but KISS for now. Exceptions are next unit.
    # also assuming that principal is an int not a float based on the test cases in the program pdf.
    principal = int(input("Enter the amount of money (principal) you will be investing: $"))
    rate = int(input("Enter the annual interest rate (a value of 5 = 5% annual interest): "))
    years = int(input("Enter the whole number of years you will be investing: "))

    # calculate interest
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
    menu_choice = ""  # prime the loop so it doesn't fail on first iteration
    # loop until user enters x
    while menu_choice != "x":
        # print menu intro message
        print("**  Interest Value Calculator  **")
        # get user input for menu choice
        menu_choice: str = input(
            "C: Calculate Interest\nD: Display Interest Information\nX: Exit\nUser Input: ",
        ).lower()  # cast it to lower so we dont have to compare both cases
        if menu_choice in ("c", "d", "x"):  # validate input against menu options
            if menu_choice == "c":  # if menu_choice is "c"
                # call TotalAccount(), store results into interest and total
                interest, total = TotalAccount()

                # print the interest and total account value
                print(
                    f"\nTotal Interest Earned: ${interest:.2f}\n"
                    f"Total Account Value:   ${total:.2f}\n",
                )

            # if menu_choice is "d" then display information
            elif menu_choice == "d":
                DisplayInfo()


main()

# =========Comments/Explanation of code from outside the lectures=========
# I was originally using the program requirements from the assignment PDF as as comments on the functions.
# they were basically documenting the functions so I figured why not just practice putting the information in docstrings
# I used the google style guide for python for the docstrings.
# https://google.github.io/styleguide/pyguide.html#383-functions-and-methods
