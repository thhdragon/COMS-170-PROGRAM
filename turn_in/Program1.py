# Tyler Hill
# 0506760
# Program 1
# COMS-170-01: Winter 2026
# Due: 1/23/26
# Program 1 - This application stores and prints information about me.
# Stores 5 variables, prints 5 statements.
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
# MY_NAME               str         store my name
# DEGREE_PROGRAM        str         store my degree program
# JOB_GOAL              str         store my goal after college (job title)
# GRADUATION_DATE       str         store my anticipated graduation date in (month/year) format
# FAVORITE_CHARACTER    str         store my favorite fictional character (ie. cartoon/animated)

# Create variables and assign values
MY_NAME: str = "Tyler Hill"
DEGREE_PROGRAM: str = "Computer Information Systems"
JOB_GOAL: str = "Software Engineer"
GRADUATION_DATE: str = "9/2027"
FAVORITE_CHARACTER: str = "The Flash"

# Display output to user
print(f"My name is {MY_NAME}.")
print(f"I am enrolled in the {DEGREE_PROGRAM} program.")
print(f"My goal after college is to be a {JOB_GOAL}.")
print(f"My anticipated graduation date is {GRADUATION_DATE}.")
print(f"My favorite fictional character is {FAVORITE_CHARACTER}.")

# Add Output of final program as Comments

# = RESTART: C:/Users/Tyler/Documents/MCC/Winter-2026/COMS-170/Week1/COMS-170-program_1.py
# My name is Tyler Hill.
# I am enrolled in the Computer Information Systems program.
# My goal after college is to be a Software Engineer.
# My anticipated graduation date is 9/2027.
# My favorite fictional character is The Flash.


# Citations/Explanations

# f-strings
# I dont know if f-strings are considered something that needs a
# citation in modern python I like them because they are cleaner especially when
# you need a variable inbetween text in a string. I read through more of the book
# this weekend and it looks like they are mentioned in chapter 6 https://www.py4e.com/html3/06-strings

# type hints
# In your lecture video you had explained types and also naming
# variables with labels so I gave my constants type hints. I know python doesn't
# actually care about type hints and that it would have inferred that the values
# were strings because of the double quotes. I'm just personally trying to
# practice common conventions and PEP rules.
