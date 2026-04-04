# Tyler Hill
# 0506760
# Program 8
# COMS-170-01: Winter 2026
# Due: 05/06/26
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


def main() -> None:
    final_as_list: list[str] = []
    text_from_user: str = input("Enter your sentences: ")
    sentences: list[str] = text_from_user.split(".")

    for sentence in sentences:
        sentence_clean: str = sentence.strip()

        if not sentence_clean:
            continue
        final_as_list.append(sentence_clean[0].upper() + sentence_clean[1:])

    final_as_str: str = ". ".join(final_as_list)

    if text_from_user.endswith("."):
        print(f"{final_as_str}.")
    else:
        print(final_as_str)


main()
