# Tyler Hill
# 0506760
# Program 5
# COMS-170-01: Winter 2026
# TODO: Due: xx/xx/26
# TODO: Program description
# ------------------------------------------------------------------
# Variable      Type        Purpose
# ------------------------------------------------------------------
#
# ------------------------------------------------------------------

# menu() ->type is str or None because it only returns a string on valid user input
# only returns None if the user input was invalid
def menu() -> str | None:
    # print menu intro message
    print("**  Interest Value Calculator  **")

    # get user input for menu choice
    menu_choice: str = input(
        "C: Calculate Interest\nD: Display Interest Information\nX: Exit\nUser Input: ",
    )

    # validate user input
    # could inline but this is easier to read
    # check if the menu_choice is `in` a list of C D or X (technically a tuple) and return true or false
    # cast to lowercase so the user can enter in whatever case because for this program we don't care if it was C or c
    valid: bool = menu_choice.lower() in ("c", "d", "x")
    if not valid:
        # if user input was invalid, print the user's input back to them with along with an error message
        print(
            f"\n{menu_choice.upper()} is not a valid option please reread the instructions\n",
        )
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
    print(
        """
        Enter the interest rate entered as a percentage
        (e.g., enters 6 for 6% interest)
        and the number of years the money will be invested.
        """,
    )

    principal: str = input(
        "Enter the amount of money (principal) you will be investing: $",
    )
    # simple way to get back to the main menu
    if principal.lower() == "x":
        return None
    rate: str = input(
        "Enter the annual interest rate (a value of 5 = 5% annual interest): ",
    )
    years: str = input("Enter the whole number of years you will be investing: ")

    if not principal.isdigit() or not rate.isdigit() or not years.isdigit():
        print(
            f"""
            {"=" * 25}ERROR{"=" * 25}

            One or multiple of
            'principal: ({principal})',
            'rate: ({rate})',
            or 'years: ({years})'
            are invalid.
            {"=" * 55}
            """,
        )
        return None

    interest = CalcInterest(
        int(principal),
        int(rate),
        int(years),
    )
    # divide interest by 100 because used integers for rate %
    interest: float = interest / 100
    # add interest to principal to get total
    total_account: float = int(principal) + interest

    return interest, total_account


def DisplayInfo() -> None:  # noqa: N802
    print(
        """
    The simple interest formula is:

    Interest = Principal x Rate x Time

    The Principal is the amount of money invested.
    The Rate is the annual interest rate the money will earn.
    The Time is the number of years the money will be invested for.
    """,
    )


def main() -> None:
    # create an empty string for menu_choice so the while loop has something to check against
    menu_choice: str = ""
    while menu_choice != "x":
        reply: str | None = menu()
        # if the user input was invalid, continue to next loop iteration
        if reply is None:
            continue
        menu_choice = reply

        if menu_choice == "c":
            from_total_account: tuple[float, float] | None = TotalAccount()
            if from_total_account is None:
                continue
            interest, total = from_total_account

            print(f"""
                Total Interest Earned: ${interest:.2f}
                Total Account Value:   ${total:.2f}
                """)

        elif menu_choice == "d":
            DisplayInfo()


main()
