# Tyler Hill
# 0506760
# Program 5
# COMS-170-01: Winter 2026
# Due: 03/20/26
# Program description: Program prompts user for account interest values
# and calculates the total interest earned and the total account value.
# ------------------------------------------------------------------
# Variable       Type        Purpose
# ------------------------------------------------------------------
# principal      int         amount of money to invest. user input
# rate           int         interest rate % as a whole number. user input
# years          int         number of years to invest. user input
# interest       float       amount of interest earned. calculated
# total_account  float       total amount of money in the account. calculated
# menu_choice    str         user input for menu choice
# ------------------------------------------------------------------


def CalcInterest(principal: int, rate: int, years: int) -> float:
    """Calculate interest from user input.

    Calculates interest by multiplying the principal, rate, and time. (interest = principal * rate * time)

    Args:
        principal (int): initial amount of money used to calculate interest.
        rate (int): annual interest rate in percentage.
        years (int): number of years used to calculate interest. called years to not shadow time module.

    Returns:
        float: the amount of interest earned. return is divided by 100 to convert from percentage to decimal

    """
    return (principal * rate * years) / 100


def TotalAccount() -> tuple[float, float]:
    """Prompts user for input sends to CalcInterest.

    Prompts user for principal, rate, and years. Then passes values to CalcInterest.
    Input strings are cast to integers and the input is assumed to be valid.

    Args:
        None

    Returns:
        tuple[float, float]: a tuple containing the interest earned and the total account value.
        The first value is the interest earned and the second value is the total account value.

    """
    print("""
Enter the interest rate entered as a percentage
(e.g., enters 6 for 6% interest)
and the number of years the money will be invested.
""")

    # casting an input() string to int can fail with ValueError if the string isn't valid numbers.
    # this should go into a try/except block but KISS for now. Exceptions are next unit.
    # also assuming that principal is an integer not a float based on the test cases from the assignment pdf.
    principal = int(input("Enter the amount of money (principal) you will be investing: $"))
    rate = int(input("Enter the annual interest rate (a value of 5 = 5% annual interest): "))
    years = int(input("Enter the whole number of years you will be investing: "))

    # calculate interest
    interest = CalcInterest(
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
    print("""
The simple interest formula is:
Interest = Principal x Rate x Time
The Principal is the amount of money invested.
The Rate is the annual interest rate the money will earn.
The Time is the number of years the money will be invested for.
""")


def main() -> None:
    """Display menu and handle user input."""
    # create menu_choice so the while loop has something to check against
    # print menu intro message
    print("**  Interest Value Calculator  **")

    # prime the loop so it doesn't fail on first iteration
    menu_choice = ""
    # loop until user enters x
    while menu_choice != "x":
        # get user input for menu choice. cast it to lower so we dont have to compare both cases
        menu_choice: str = input(
            "C: Calculate Interest\nD: Display Interest Information\nX: Exit\nUser Input: ",
        ).lower()
        if menu_choice in ("c", "d", "x"):
            # if menu_choice is "c" then calculate interest
            if menu_choice == "c":
                # call TotalAccount(), destructure the tuple into interest and float
                interest, total = TotalAccount()

                # print the interest and total account value
                print(f"\nTotal Interest Earned: ${interest:.2f}\nTotal Account Value:   ${total:.2f}\n")

            # if menu_choice is "d" then display information
            elif menu_choice == "d":
                DisplayInfo()


main()
