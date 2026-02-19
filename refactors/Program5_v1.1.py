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

from dataclasses import dataclass


# put data into a struct so its much less confusing with free floating variables.
@dataclass
class AccountInterest:
    principal: int
    rate: int
    years: int
    interest: float
    value: float

    # when in Rome do as the pythonistas do i guess
    def calc_interest(self) -> None:
        # Interest = (Principal x Rate x Time) then / 100 because we took rate % as an int
        self.interest = (self.principal * self.rate * self.years) / 100


def menu() -> str | None:
    # print menu intro message
    print("**  Interest Value Calculator  **")
    menu_choice: str = input(
        "C: Calculate Interest\nD: Display Interest Information\nX: Exit\nUser Input: ",
    )

    valid: bool = menu_choice.lower() in ("c", "d", "x")
    if not valid:
        print(f"\n{menu_choice.upper()} is not a valid option please reread the instructions\n")
        return None

    return menu_choice.lower()


def CalcInterest(principal: int, rate: int, years: int) -> int:  # noqa: N802
    return principal * rate * years


def TotalAccount() -> tuple[float, float] | None:  # noqa: N802
    from_input: tuple[int, int, int] | None = get_account_input()
    if from_input is None:
        return None
    principal, rate, years = from_input
    interest = CalcInterest(
        principal,
        rate,
        years,
    )
    # divide interest by 100 because used integers for rate %
    interest: float = interest / 100
    # add interest to principal to get total
    total_account: float = principal + interest

    return interest, total_account


# function to get interest rate and percentage from user and n number of years to invest
def get_account_input() -> tuple[int, int, int] | None:
    print("""
    Enter the interest rate entered as a percentage
    (e.g., enters 6 for 6% interest)

    and the number of years the money will be invested.
    """)

    principal: str = input("Enter the amount of money (principal) you will be investing: $")

    # simple way to get back to the main menu
    if principal.lower() == "x":
        return None

    rate: str = input("Enter the annual interest rate (a value of 5 = 5% annual interest): ")

    years: str = input("Enter the whole number of years you will be investing: ")

    # validate input and retry if invalid
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
        return get_account_input()

    return int(principal), int(rate), int(years)


def DisplayInfo() -> None:  # noqa: N802
    print("""
    The simple interest formula is:

    Interest = Principal x Rate x Time

    The Principal is the amount of money invested.
    The Rate is the annual interest rate the money will earn.
    The Time is the number of years the money will be invested for.
    """)


def display_results(interest: float, total: float) -> None:
    print(f"""
    Total Interest Earned: ${interest:.2f}
    Total Account Value:   ${total:.2f}
    """)


def main() -> None:
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

            display_results(interest, total)

        elif menu_choice == "d":
            DisplayInfo()


main()
