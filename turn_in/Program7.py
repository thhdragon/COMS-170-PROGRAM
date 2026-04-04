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
# comp_times       list[float]   list of completion times entered by the user
# time_as_str      str           current completion time as a string from user input
# time_as_float    float         current completion time as a float after conversion
# fastest          float         fastest completion time from the list
# slowest          float         slowest completion time from the list
# average          float         average completion time from the list
# empty            str           error message for empty input
# negative         str           error message for negative input
# not_finite       str           error message for non-finite input
# too_long         str           error message for input > 999999.99
# --------------------------------------------------------------------------------
from math import isfinite


# use the None to orchestrate error handling in main
def time_str_to_float(time_as_str: str) -> float:
    """Try to convert a string into a valid time value, can fail."""
    # check if the input is an empty string
    if time_as_str == "":
        empty = "Completion time can't be empty"
        raise ValueError(empty)
    # cast time_as_str to a float and put value in time_as_float (can fail)
    time_as_float = float(time_as_str)
    # use a match statement to check for different conditions because it's easier to read
    # guard to return -1.0 if the user enters -1 to compute the results
    if time_as_float == -1.0:
        return -1.0
    # guard to error if the user enters a negative number
    # check if input value is greater than or equal to 0
    if time_as_float <= 0.0:
        negative = "Completion time can't be 0 or negative"
        raise ValueError(negative)
    # guard to error if the user enters a non-finite number
    # check if input value is not finite with the math.isfinite() function
    # this safeguards against +- inf and nan
    if not isfinite(time_as_float):
        not_finite = "Completion time must be a finite number"
        raise ValueError(not_finite)
    # guard to error if the user enters a number longer than 999999.99
    # need some sort of upper bound to prevent formatting issues
    if time_as_float > 999999.99:
        too_long = "if you take over 11 days you don't get on the list"
        raise ValueError(too_long)
    # if it makes it here its probably valid
    return time_as_float


def main() -> None:
    # print the title
    print(
        "<><><><><><><><><><><><><><><><><>\n"
        "<        MUCSOCS eSports         >\n"
        "<><><><><><><><><><><><><><><><><>\n\n"
        "Completion Time Information\n",
    )
    # initialize variables outside the loop so they stay alive after the loop ends
    comp_times: list[float] = []
    time_as_float = 0.0
    # while loop to keep the program running until the user enters -1
    while time_as_float != -1.0:
        # use input() to get the completion time and store it in time_as_str
        time_as_str: str = input("Enter completion time (in seconds) or -1 to calculate results: ")
        # call time_str_to_float() and put its reply in variable time_as_float (can fail)
        try:
            time_as_float: float = time_str_to_float(time_as_str)
        except ValueError as err:
            print(f"'{time_as_str}' is an invalid input: {err}")
            continue

        if time_as_float == -1:
            continue
        comp_times.append(time_as_float)

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
