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

# put data into a dict because im a simp for structs
dice_data: dict[str, int] = {
    "goal": 12,
    "die_1": 0,
    "die_2": 0,
    "sum_of_current_roll": 0,
    "current_roll_count": 0,
    "sum_of_total_rolls": 0,
}

# create intro
INTRO_MSG: str = f"{'*' * 28}\n*{' ' * 4}Random Dice Roller{' ' * 4}*\n{'*' * 28}"


def roll_dice() -> None:
    dice_data["die_1"] = randint(1, 6)
    dice_data["die_2"] = randint(1, 6)
    dice_data["sum_of_current_roll"] = dice_data["die_1"] + dice_data["die_2"]
    # increase index tracking the total number of rolls
    dice_data["current_roll_count"] += 1


def main() -> None:
    # print intro
    print(INTRO_MSG)

    while dice_data["sum_of_current_roll"] != dice_data["goal"]:
        # Roll dice
        roll_dice()
        print(
            f"{dice_data['current_roll_count']:2}.)  Dice: {dice_data['die_1']} - {dice_data['die_2']}  Total: {dice_data['sum_of_current_roll']}",
        )

        # track how many times its called and track the total dice values summed
        dice_data["sum_of_total_rolls"] += dice_data["sum_of_current_roll"]

    # sum of total rolls divided by amount of rolls
    print(f"Rolls:   {dice_data['current_roll_count']}")
    print(f"Average: {(dice_data['sum_of_total_rolls'] / dice_data['current_roll_count']):.2f}")


main()

# ----------------------------------------
# Add Output of final program as Comments
# ----------------------------------------

# --------------------------
# Additional notes/comments
# --------------------------
