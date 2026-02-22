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
# init variables to 0
current_roll_count: int = 0
sum_all_rolls: int = 0
roll_total: int = 0
# create intro
INTRO_MSG: str = f"{'*' * 28}\n*{' ' * 4}Random Dice Roller{' ' * 4}*\n{'*' * 28}"

# print intro
print(INTRO_MSG)

# Roll dice
while roll_total != GOAL:
    die_1: int = randint(1, 6)
    die_2: int = randint(1, 6)
    roll_total: int = die_1 + die_2
    current_roll_count += 1
    sum_all_rolls += roll_total
    print(f"{current_roll_count:2}.)  Dice: {die_1} - {die_2}  Total: {roll_total}")

average_of_roll_sum_total: float = sum_all_rolls / current_roll_count
print(f"Rolls:   {current_roll_count}")
print(f"Average: {average_of_roll_sum_total:.2f}")


# ----------------------------------------
# Add Output of final program as Comments
# ----------------------------------------

# --------------------------
# Additional notes/comments
# --------------------------
