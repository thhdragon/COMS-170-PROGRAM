# Tyler Hill
# 0506760
# Program 7
# COMS-170-01: Winter 2026
# Due: 04/20/26
# Program description: takes a list of completion times from user input and calculates
# the fastest, slowest, and average completion times
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


# function try_into_time (input: time from the input function (time_str)) (output: float on success | None on failure)
# use the None to orchestrate error handling in main
def try_into_time(time_str: str) -> float | None:
    """Try to convert a string into a valid time value, return None if it fails."""
    # open a try block because converting a string to a float can fail on non numeric characters (jump to except ValueError)
    try:
        # cast time_str to a float and put value in time_float
        time_float = float(time_str)
        # use a match statement to check for different conditions because it's more readable than a bunch of ifs
        match time_float:
            # case to return -1.0 if the user enters -1 to compute the results
            case -1.0:
                return -1.0
            # case to return None if the user enters a negative number
            # check if input value is greater than or equal to 0
            case negative if negative <= 0.0:
                print("Completion time can't be 0 or negative")
                return None
            # case to return None if the user enters a non-finite number
            # check if input value is not finite with the math.isfinite() function
            # this safeguards against +- inf and nan
            case not_finite if not isfinite(not_finite):
                print("Completion time must be a finite number")
                return None
            # case to return None if the user enters a number longer than 999999.99
            # need some sort of upper bound to prevent formatting issues
            case too_long if too_long > 999999.99:
                print("if you take over 11 days you don't get on the list")
                return None
            # i cant think of any more conditions to check so if it makes it here its probably valid
            # case to return the "hopefully valid" time_float
            case _:
                return time_float

    # if the string can't be converted to a float (jump here)
    # ValueError is raised when the string can't be converted to a float
    # set custom behavior for ValueError exceptions
    # print invalid input back to user and return None
    except ValueError:
        print(f"{time_str} is not a valid input")
        return None


# function main (input: no input) (output: None)
def main() -> None:
    # print the title
    print(
        "<><><><><><><><><><><><><><><><><>\n"
        "<        MUCSOCS eSports         >\n"
        "<><><><><><><><><><><><><><><><><>\n\n"
        "Completion Time Information\n",
    )
    # initialize variables comp_times and new_time outside the loop so they stay alive after the loop ends
    comp_times: list[float] = []
    new_time = 0.0
    # while loop to keep the program running until the user enters -1
    while new_time != -1.0:
        # use input() to get the completion time and store it in time_str
        time_str: str = input("Enter completion time (in seconds) or -1 to calculate results: ")
        # call try_into_time() and put its reply in variable result
        result: float | None = try_into_time(time_str)
        # use a match statement to check for different conditions
        match result:
            # if try_into_time fails it returns None so skip to the next iteration
            case None:
                continue
            # if try_into_time returns -1 set new_time to the returned value signaling quit
            case -1.0:
                new_time = result
            # if try_into_time returns a valid number append it to the comp_times list
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
