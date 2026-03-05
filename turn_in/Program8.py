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


final_as_list: list[str] = []
test_input: str = "my name is Samantha. i go to Mott Community College."
sentences: list[str] = test_input.split(".")
for sentence in sentences:
    sentence_clean: str = sentence
    sentence_clean = sentence_clean.strip()
    if not sentence_clean:
        continue
    else:
        final_as_list.append(sentence_clean[0].upper() + sentence_clean[1:])

final_as_str: str = ". ".join(final_as_list)

if test_input.endswith("."):
    print(f"{final_as_str}.")
else:
    print(final_as_str)
