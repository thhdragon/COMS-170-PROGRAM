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
class DiceResults:
    die_1: int = 0
    die_2: int = 0
    sum_of_current_roll: int = 0
    current_roll_count: int = 0
    sum_of_total_rolls: int = 0
    average_from_rolls: float = 0.0
    goal: int = 12

    def roll_dice(self) -> None:
        self.die_1 = randint(1, 6)
        self.die_2 = randint(1, 6)
        self.sum_of_current_roll = self.die_1 + self.die_2
        # increase index tracking the total number of rolls
        self.current_roll_count += 1


def main() -> None:
    # print intro
    print(INTRO_MSG)
    # create instance of dataclass DiceStats
    results = DiceResults()

    while results.sum_of_current_roll != results.goal:
        # Roll dice
        results.roll_dice()
        print(
            f"{results.current_roll_count:2}.)  Dice: {results.die_1} - {results.die_2}  Total: {results.sum_of_current_roll}",
        )

        # add the current roll to the running sum total
        results.sum_of_total_rolls += results.sum_of_current_roll

    results.average_from_rolls = results.sum_of_total_rolls / results.current_roll_count
    # sum of total rolls divided by amount of rolls
    print(f"Rolls:   {results.current_roll_count}")
    print(f"Average: {results.average_from_rolls:.2f}")


main()

# ----------------------------------------
# Add Output of final program as Comments
# ----------------------------------------


# --------------------------
# Additional notes/comments
# --------------------------
