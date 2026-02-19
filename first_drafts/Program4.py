# Tyler Hill
# 0506760
# Program 4
# COMS-170-01: Winter 2026
# Due: 2/27/26
# Program simulates rolling a pair of 6-sided dice until a total of 12 is rolled,
# prints roll number, value for each die, and total.
# prints total number of rolls and average.
# ------------------------------------------------------------------
# Variable      Type        Purpose
# ------------------------------------------------------------------
#
# ------------------------------------------------------------------
from random import randint

# define magic number constants
GOAL: int = 12

# create intro
INTRO_MSG: str = f"{'*' * 28}\n*{' ' * 4}Random Dice Roller{' ' * 4}*\n{'*' * 28}"


def roll_dice() -> tuple[int, int, int]:
    die_1: int = randint(1, 6)
    die_2: int = randint(1, 6)
    total: int = die_1 + die_2
    return die_1, die_2, total


def main() -> None:
    # print intro
    print(INTRO_MSG)

    # init variables to 0
    current_roll_count: int = 0
    total_roll_sum: int = 0

    # Roll dice
    current_roll: tuple[int, int, int] = roll_dice()
    current_roll_count += 1
    total_roll_sum += current_roll[2]
    print(f"{current_roll_count:2}.)  Dice: {current_roll[0]} - {current_roll[1]}  Total: {current_roll[2]}")

    while current_roll[2] != GOAL:
        current_roll = roll_dice()
        current_roll_count += 1
        total_roll_sum += current_roll[2]
        print(f"{current_roll_count:2}.)  Dice: {current_roll[0]} - {current_roll[1]}  Total: {current_roll[2]}")

    average_of_total_roll_sum: float = total_roll_sum / current_roll_count
    print(f"Rolls:   {current_roll_count}")
    print(f"Average: {average_of_total_roll_sum:.2f}")


# ----------------------------------------
# Add Output of final program as Comments
# ----------------------------------------

# --------------------------
# Additional notes/comments
# --------------------------
