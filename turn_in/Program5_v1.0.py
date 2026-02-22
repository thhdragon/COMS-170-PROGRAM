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
# menu_choice    str         user input for menu choice
# principal      int         user input for principal amount
# rate           int         user input for rate
# years          int         user input for years
# interest       float       calculated interest
# total_account  float       calculated total account value
# ------------------------------------------------------------------

# menu() ->type is str or None because it only returns a string on valid user input
# only returns None if the user input was invalid
def menu() -> str | None:
    # print menu intro message
    print("**  Interest Value Calculator  **")

    # get user input for menu choice
    menu_choice: str = input("C: Calculate Interest\nD: Display Interest Information\nX: Exit\nUser Input: ")

    # validate user input
    # could inline but this is easier to read
    # check if the menu_choice is `in` a list of C D or X (technically a tuple) and return true or false
    # cast to lowercase so the user can enter in whatever case because for this program we don't care if it was C or c
    valid: bool = menu_choice.lower() in ("c", "d", "x")
    if not valid:
        # if user input was invalid, print the user's input back to them with along with an error message
        print(f"\n{menu_choice.upper()} is not a valid option please reread the instructions\n")
        # return None early to the main loop because we didn't get a valid input
        return None

    # if menu_choice makes it past the check then return it to the caller.
    return menu_choice.lower()


# CalcInterest() ->type is int
# values already validated by the time this function is called
def CalcInterest(principal: int, rate: int, years: int) -> int:
    # formula is simple enough to inline in the return
    return principal * rate * years


# TotalAccount() ->type is tuple[float, float] or None. tuples are basically arrays
# returns None if the user input was invalid
def TotalAccount() -> tuple[float, float] | None:
    prompt_msg = """
Enter the interest rate entered as a percentage
(e.g., enters 6 for 6% interest)
and the number of years the money will be invested.
"""
    print(prompt_msg)

    # get user input for principal, rate, and years
    principal_str: str = input("Enter the amount of money (principal) you will be investing: $")
    rate_str: str = input("Enter the annual interest rate (a value of 5 = 5% annual interest): ")
    years_str: str = input("Enter the whole number of years you will be investing: ")

    # validate user input
    if not principal_str.isdigit() or not rate_str.isdigit() or not years_str.isdigit():
        err_msg = f"""
{"=" * 25}ERROR{"=" * 25}
One or multiple of:
'principal: ({principal_str})', 'rate: ({rate_str})', or 'years: ({years_str})'
are invalid.
{"=" * 55}
"""
        print(err_msg)
        # return None and skip the rest of the function
        return None

    # cast the string variables to integers
    principal: int = int(principal_str)
    rate: int = int(rate_str)
    years: int = int(years_str)

    # calculate interest
    interest = CalcInterest(
        principal,
        rate,
        years,
    )

    # divide interest by 100 because used integers for rate %
    interest: float = interest / 100

    # add interest to principal to get total
    total_account: float = principal + interest

    # return the interest and total account value
    return interest, total_account


def DisplayInfo() -> None:
    info = """
The simple interest formula is:
Interest = Principal x Rate x Time
The Principal is the amount of money invested.
The Rate is the annual interest rate the money will earn.
The Time is the number of years the money will be invested for.
"""
    print(info)


def main() -> None:
    # create menu_choice so the while loop has something to check against
    menu_choice: str | None = None

    # loop until user enters x
    while menu_choice != "x":
        # could use walrus operator here but it's not as readable
        menu_choice = menu()

        # if the valid choice check fails in menu() it returns None here
        # use that Some or None to control the flow of the loop
        # if we get None here it means the user entered invalid input
        # so if None we can say skip the rest of the loop and run the next iteration
        if menu_choice is None:
            continue

        # if menu_choice is "c" then calculate interest
        if menu_choice == "c":
            # call TotalAccount() and store the return value in from_total_account
            # return into a single variable to be able to check for None
            from_total_account: tuple[float, float] | None = TotalAccount()

            # if from_total_account is None then skip the rest of the loop and run the next iteration
            if from_total_account is None:
                continue

            # now if from_total_account is not None then we can unpack the tuple
            interest, total = from_total_account

            # print the interest and total account value
            print(f"Total Interest Earned: ${interest:.2f}\nTotal Account Value:   ${total:.2f}\n")

        # if menu_choice is "d" then display information
        elif menu_choice == "d":
            DisplayInfo()


main()
