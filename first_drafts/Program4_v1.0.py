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
sum_of_current_roll: int = 0
sum_of_all_rolls: int = 0
current_roll_count: int = 0

# create intro
INTRO_MSG: str = f"{'*' * 28}\n*{' ' * 4}Random Dice Roller{' ' * 4}*\n{'*' * 28}"
# print intro
print(INTRO_MSG)

# main loop to roll dice
# while sum of current roll is not equal to GOAL
# while die 1 + die 2 is not 12
while sum_of_current_roll != GOAL:
    # use the randint method from the random module to get random values for die_1 and die_2
    die_1: int = randint(1, 6)
    die_2: int = randint(1, 6)

    # Add die to get sum of current roll
    sum_of_current_roll: int = die_1 + die_2

    # increment the counter that says we just did a "virtual" dice roll.
    current_roll_count += 1

    # add the sum of the current roll to the total sum from all rolls
    # sum total = sum total + sum of new roll
    sum_of_all_rolls += sum_of_current_roll

    # print out per roll results
    print(f"{current_roll_count:2}.)  Dice: {die_1} - {die_2}  Total: {sum_of_current_roll}")

# after the loop condition becomes valid get the average from dividing sum of all rolls and roll count
average_from_roll_sum_total: float = sum_of_all_rolls / current_roll_count
print(f"Rolls:   {current_roll_count}")
print(f"Average: {average_from_roll_sum_total:.2f}")


# ----------------------------------------
# Add Output of final program as Comments
# ----------------------------------------

# --------------------------
# Additional notes/comments
# --------------------------
