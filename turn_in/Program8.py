# Tyler Hill
# 0506760
# Program 8
# COMS-170-01: Winter 2026
# Due: 04/17/26
# Program description: takes a string of sentences and capitalizes the first letter of each sentence
# --------------------------------------------------------------------------------
# Variable          Type          Purpose
# --------------------------------------------------------------------------------
# final_as_list     list[str]     holds the final list of sentences
# text_from_user    str           holds the text from the user
# sentences         list[str]     holds the list of sentences
# sentence          str           holds the current sentence
# sentence_clean    str           holds the cleaned sentence
# final_as_str      str           holds the final string
# --------------------------------------------------------------------------------
# An example of input is: my name is Samantha. i go to Mott Community College.
# The output would be: My name is Samantha. I go to Mott Community College.

# Program written in Python containing:
# a. Input for the user to enter their sentences.
# b. Conversion of input to list items based on end of sentence period.
# c. Modification of each list item to capitalize the first character of the string while leaving
# the remainder of the string as is.
# d. Concatenation of the values in the list to a single string.
# e. Output of the final string.
# f. Program is saved as Program8.py

# set a constant for the welcome message and prompt strings
WELCOME: str = (
    "--Sentence Capitalizer--\n"
    "An example of input is: my name is Samantha. i go to Mott Community College.\n"
    "The output would be: My name is Samantha. I go to Mott Community College.\n"
)
PROMPT: str = "Enter your sentences: \n"


def main() -> None:
    # print welcome message
    print(WELCOME)
    # create an empty list
    final_as_list: list[str] = []
    # get the sentence from the user
    text_from_user: str = input(PROMPT)
    # split the sentence into a list of sentence strings by the period character
    sentences: list[str] = text_from_user.split(".")

    # loop through the list of sentences
    for sentence in sentences:
        # strip the sentence of whitespaces
        sentence_clean: str = sentence.strip()

        # check if the sentence is empty
        if not sentence_clean:
            # skip it if its empty
            continue
        # append to the final list
        # use array index notation to grab the char at index 0 and capitalize it
        # use string slice notation to grab the string starting at index 1 to the end
        # concatenate the two together and append to the final list
        final_as_list.append(sentence_clean[0].upper() + sentence_clean[1:])

    # join the list of sentences together using '. ' as the separator
    final_as_str: str = ". ".join(final_as_list)

    # check if the original text ends with a period
    if text_from_user.endswith("."):
        # if it ends with a period add a period at the end when printing it
        print(f"{final_as_str}.")
    # else print as is
    else:
        print(final_as_str)


main()
