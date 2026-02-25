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
#
# ------------------------------------------------------------------


def CalcInterest(principal: int, rate: int, years: int) -> int:
    return principal * rate * years


def TotalAccount() -> tuple[float, float]:
    print("""
Enter the interest rate entered as a percentage
(e.g., enters 6 for 6% interest)
and the number of years the money will be invested.
""")

    # get user input for principal, rate, and years. assume user enters valid integers.
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

    # used integers input for rate % so divide interest by 100
    interest: float = interest / 100

    # add interest to principal to get total
    total_account: float = principal + interest

    # return the interest and total account value
    return interest, total_account


def DisplayInfo() -> None:
    print("""
The simple interest formula is:
Interest = Principal x Rate x Time
The Principal is the amount of money invested.
The Rate is the annual interest rate the money will earn.
The Time is the number of years the money will be invested for.
""")


def main() -> None:
    # create menu_choice so the while loop has something to check against
    # print menu intro message
    print("**  Interest Value Calculator  **")

    # prime the loop so it doesn't fail on first iteration
    menu_choice = ""
    # loop until user enters x
    while menu_choice.lower() != "x":
        # get user input for menu choice
        menu_choice: str = input("C: Calculate Interest\nD: Display Interest Information\nX: Exit\nUser Input: ")
        if menu_choice.lower() in ("c", "d", "x"):
            # if menu_choice is "c" then calculate interest
            if menu_choice == "c":
                # call TotalAccount(), destructure the tuple into interest and float
                interest, total = TotalAccount()

                # print the interest and total account value
                print(f"Total Interest Earned: ${interest:.2f}\nTotal Account Value:   ${total:.2f}\n")

            # if menu_choice is "d" then display information
            elif menu_choice == "d":
                DisplayInfo()


main()
