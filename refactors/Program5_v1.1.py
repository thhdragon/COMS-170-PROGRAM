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
class Account:
    principal: int = 0
    rate: int = 0
    years: int = 0
    interest: float = 0
    total_value: float = 0

    # when in Rome do as the pythonistas do i guess
    def calc_interest(self) -> None:
        # Interest = (Principal x Rate x Time) then / 100 because we took rate % as an int
        self.interest = (self.principal * self.rate * self.years) / 100

    def total_account(self) -> None:
        from_input: tuple[int, int, int] | None = get_account_input()
        if from_input is None:
            return
        self.principal, self.rate, self.years = from_input
        self.calc_interest()
        self.total_value = self.principal + self.interest

    def display_results(self) -> None:
        print(f"""
        Total Interest Earned: ${self.interest:.2f}
        Total Account Value:   ${self.total_value:.2f}
        """)


@dataclass
class UserInputStrings:
    principal_str: str
    rate_str: str
    years_str: str

    def prompt_user(self) -> None:
        print("""
        Enter the interest rate entered as a percentage
        (e.g., enters 6 for 6% interest)

        and the number of years the money will be invested.
        """)
        self.principal_str = input("Enter the amount of money (principal) you will be investing: $")
        if self.principal_str == "x":
            return
        self.rate_str = input("Enter the annual interest rate (a value of 5 = 5% annual interest): ")
        self.years_str = input("Enter the whole number of years you will be investing: ")

    def validate(self) -> bool:
        if not self.principal_str.isdigit() or not self.rate_str.isdigit() or not self.years_str.isdigit():
            print(
                f"""
            {"=" * 5}ERROR{"=" * 5}

            One or multiple of
            'principal: ({self.principal_str})',
            'rate: ({self.rate_str})',
            or 'years: ({self.years_str})'
            are invalid.
            {"=" * 25}
            """,
            )
            return False
        return True


def menu() -> str | None:
    # print menu intro message
    print("**  Interest Value Calculator  **")
    choice: str = input("C: Calculate Interest\nD: Display Interest Information\nX: Exit\nUser Input: ")

    valid: bool = choice.lower() in ("c", "d", "x")
    if not valid:
        print(f"\n{choice.upper()} is not a valid option please reread the instructions\n")
        return None

    return choice.lower()


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


def main() -> None:
    acc = Account()
    menu_choice: str = ""
    while menu_choice != "x":
        reply: str | None = menu()
        # if the user input was invalid, continue to next loop iteration
        if reply is None:
            continue
        menu_choice = reply

        if menu_choice == "c":
            acc.total_account()
            acc.display_results()

        elif menu_choice == "d":
            DisplayInfo()


main()
