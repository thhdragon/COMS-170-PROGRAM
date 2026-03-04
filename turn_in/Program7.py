# Tyler Hill
# 0506760
# Program 7
# COMS-170-01: Winter 2026
# Due: 04/20/26
# Program description: todo
# --------------------------------------------------------------------------------
# Variable          Type          Purpose
# --------------------------------------------------------------------------------
# comp_times        list[float]   holds the completion times of the competitors
# new_time          float         holds the new completion time entered by the user
# time_str          str           holds the string representation of the completion time
# result            float | None  holds the result of converting time_str to a float
# fastest           float         holds the fastest completion time
# slowest           float         holds the slowest completion time
# average           float         holds the average completion time
# --------------------------------------------------------------------------------
from math import isfinite


def try_into_time(time_str: str) -> float | None:
    """Try to convert a string into a valid time value, return None if it fails."""
    try:
        time_float = float(time_str)
        match time_float:
            case -1.0:
                return -1.0
            case negative if negative <= 0.0:
                print("Completion time can't be 0 or negative")
                return None
            case not_finite if not isfinite(not_finite):
                return None
                print("Completion time must be a finite number")
            case too_long if too_long > 999999.99:
                print("if you take over 11 days you don't get on the list")
            case _:
                return time_float

    except ValueError:
        print(f"{time_str} is not a valid input")
        return None


def main() -> None:
    print(
        "<><><><><><><><><><><><><><><><><>\n"
        "<        MUCSOCS eSports         >\n"
        "<><><><><><><><><><><><><><><><><>\n\n"
        "Completion Time Information\n",
    )
    comp_times: list[float] = []
    new_time = 0.0
    while new_time != -1.0:
        # instant feedback if user enters incorrect value
        time_str: str = input("Enter completion time (in seconds) or -1 to calculate results: ")
        result: float | None = try_into_time(time_str)
        match result:
            case None:
                continue
            case -1.0:
                new_time = -1.0
            case _:
                comp_times.append(result)

    if not comp_times:
        print("No completion times added, Exiting program.")
        return

    fastest: float = min(comp_times)
    slowest: float = max(comp_times)
    # basic list methods to get average instead of statistics.fmeans()
    average: float = sum(comp_times) / len(comp_times)
    print(
        f"\nFastest completion time formatted with two decimal places: {fastest:.2f}\n"
        f"Slowest completion time formatted with two decimal places: {slowest:.2f}\n"
        f"Average completion time formatted with two decimal places: {average:.2f}\n\n"
        "All Competitor Times",
    )
    # basic list methods for indexing and array notation on the lists instead of enumerate()
    for idx in range(len(comp_times)):
        print(f"{idx + 1}: {comp_times[idx]:.2f} seconds")


main()
