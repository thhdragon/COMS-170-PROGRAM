# Tyler Hill
# 0506760
# Program 3
# COMS-170-01: Winter 2026
# Due: 2/03/26
# Program 3 - Program prompts user for light wavelength in nanometers,
# displays corresponding color and frequency value.
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
# ULTRAVIOLET_NM        int         store threshold for UV wavelen in nm
# VIOLET_NM_MAX         int         store max threshold for voilet wavelen in nm
# BLUE_NM_MAX           int         store max threshold for blue wavelen in nm
# GREEN_NM_MAX          int         store max threshold for green wavelen in nm
# YELLOW_NM_MAX         int         store max threshold for yellow wavelen in nm
# ORANGE_NM_MAX         int         store max threshold for orange wavelen in nm
# RED_NM_MAX            int         store max threshold for red wavelen in nm
# ULTRAVIOLET_MSG       str         store message for ultraviolet light
# VIOLET_MSG            str         store message for violet light
# BLUE_MSG              str         store message for blue light
# GREEN_MSG             str         store message for green light
# YELLOW_MSG            str         store message for yellow light
# ORANGE_MSG            str         store message for orange light
# RED_MSG               str         store message for red light
# INFARED_MSG           str         store message for infrared light
# INTRO_MSG             str         store introduction message
# input_wavelength_int  int         store user input wavelength in nanometers
# result                str         store result message
# ------------------------------------------------------------------


# give our magic numbers names so nobody has to guess
ULTRAVIOLET_NM: int = 380
ULTRAVIOLET_MSG: str = "You can't see it. That's Ultraviolet."

VIOLET_NM_MAX: int = 450
VIOLET_MSG: str = "Violet. 730 THz"

BLUE_NM_MAX: int = 495
BLUE_MSG: str = "Blue. 650 THz"

GREEN_NM_MAX: int = 570
GREEN_MSG: str = "Green. 565 THz"

YELLOW_NM_MAX: int = 590
YELLOW_MSG: str = "Yellow. 520 THz"

ORANGE_NM_MAX: int = 620
ORANGE_MSG: str = "Orange. 495 THz"

RED_NM_MAX: int = 750
RED_MSG: str = "Red. 440 THz"

# only check if greater than not equal to ir nm
INFARED_MSG: str = "You're beyond visible now into the Infrared range."

INTRO_MSG: str = (
    "*******************\n  Light and Magic  \n*******************\n\nColor Evaluator\n"
)

# print intro message
print(INTRO_MSG)
# get user input, assume user enters valid data. will error if not int
input_wavelength_int: int = int(
    input("Enter the wavelength of the light in nanometers (nm): "),
)

# hardcoded test case values - ensure commented out before turning in
# input_wavelength_int: int = 600
# input_wavelength_int: int = 200
# input_wavelength_int: int = 703

# Create variables and assign values
# init a string to put the result in
result: str = ""
# run comparative checks on the input to find matching color range.
# because we check top down we dont need the min values
# each if only happens if the next one doesnt succeed
if input_wavelength_int <= ULTRAVIOLET_NM:
    result = ULTRAVIOLET_MSG
# if it doesnt get picked up by UV that means it has to be > UV's max
elif input_wavelength_int <= VIOLET_NM_MAX:
    result = VIOLET_MSG
# if it doesnt get picked up by voilet that means it has to be > Violet's max
elif input_wavelength_int <= BLUE_NM_MAX:
    result = BLUE_MSG
# if it doesnt get picked up by blue that means it has to be > Blue's max
elif input_wavelength_int <= GREEN_NM_MAX:
    result = GREEN_MSG
elif input_wavelength_int <= YELLOW_NM_MAX:
    result = YELLOW_MSG
elif input_wavelength_int <= ORANGE_NM_MAX:
    result = ORANGE_MSG
elif input_wavelength_int <= RED_NM_MAX:
    result = RED_MSG
else:
    result = INFARED_MSG

# Display output to user
print(result)

# Add Output of final program as Comments
# = RESTART: C:\Users\Tyler\Documents\MCC\Winter-2026\COMS-170\Week3\Program3.py =
# *******************
#   Light and Magic
# *******************

# Color Evaluator

# Enter the wavelength of the light in nanometers (nm): 703
# Red. 440 THz
