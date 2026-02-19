# Tyler Hill
# 0506760
# Program 4 v3
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
from dataclasses import dataclass
from random import randint

# create intro
INTRO_MSG: str = f"{'*' * 28}\n*{' ' * 4}Random Dice Roller{' ' * 4}*\n{'*' * 28}"


# put data into a dataclass because im a simp for structs
# could just use a dict if stuck on python lower than 3.7 but the syntax sucks more than @dataclass
@dataclass
class DiceStats:
    die_1: int = 0
    die_2: int = 0
    sum_of_current_roll: int = 0
    current_roll_count: int = 0
    sum_of_total_rolls: int = 0
    average_from_rolls: float = 0.0
    goal: int = 12


def roll_dice(stats: type[DiceStats]) -> None:
    stats.die_1 = randint(1, 6)
    stats.die_2 = randint(1, 6)
    stats.sum_of_current_roll = stats.die_1 + stats.die_2
    # increase index tracking the total number of rolls
    stats.current_roll_count += 1


def main() -> None:
    # print intro
    print(INTRO_MSG)
    # create instance of dataclass DiceStats
    stats = DiceStats

    while stats.sum_of_current_roll != stats.goal:
        # Roll dice
        roll_dice(stats)
        print(
            f"{stats.current_roll_count:2}.)  Dice: {stats.die_1} - {stats.die_2}  Total: {stats.sum_of_current_roll}",
        )

        # add the current roll to the running sum total
        stats.sum_of_total_rolls += stats.sum_of_current_roll

    stats.average_from_rolls = stats.sum_of_total_rolls / stats.current_roll_count
    # sum of total rolls divided by amount of rolls
    print(f"Rolls:   {stats.current_roll_count}")
    print(f"Average: {stats.average_from_rolls:.2f}")


main()

# ----------------------------------------
# Add Output of final program as Comments
# ----------------------------------------


# --------------------------
# Additional notes/comments
# --------------------------
