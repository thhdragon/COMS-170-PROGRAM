# Tyler Hill
# 0506760
# Final Project
# COMS-170-01: Winter 2026
# Due: 04/24/26
# Program description: Encrypt and decrypt text using a substitution cipher
# --------------------------------------------------------------------------------
# Variable          Type          Purpose
# --------------------------------------------------------------------------------
# ALPHANUM_MAP      list[str]     map of characters to be used in the cipher
# KEY_MAP           list[str]     map of characters to be used in the cipher
# valid             tuple[str]    tuple of valid menu choices
# choice            str           user's menu choice
# plaintext_input   str           user's plaintext input
# encrypted_input   str           user's encrypted input
# parsed_list       list[str]     list of parsed characters
# parsed_char       str           parsed character
# --------------------------------------------------------------------------------

# Alphabetical and numerical map
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z . 1 2 3 4 5 6 7 8 9 0
ALPHANUM_MAP: list[str] = [
    "A",  # 0
    "B",  # 1
    "C",  # 2
    "D",  # 3
    "E",  # 4
    "F",  # 5
    "G",  # 6
    "H",  # 7
    "I",  # 8
    "J",  # 9
    "K",  # 10
    "L",  # 11
    "M",  # 12
    "N",  # 13
    "O",  # 14
    "P",  # 15
    "Q",  # 16
    "R",  # 17
    "S",  # 18
    "T",  # 19
    "U",  # 20
    "V",  # 21
    "W",  # 22
    "X",  # 23
    "Y",  # 24
    "Z",  # 25
    ".",  # 26
    "1",  # 27
    "2",  # 28
    "3",  # 29
    "4",  # 30
    "5",  # 31
    "6",  # 32
    "7",  # 33
    "8",  # 34
    "9",  # 35
    "0",  # 36
]

# Key map for encryption/decryption
# H 1 N V 7 B L 0 R I 3 F P 4 S U A X 2 E 8 O 9 G K 5 W C Q 6 J Y . D T Z M
KEY_MAP: list[str] = [
    "H",  # 0
    "1",  # 1
    "N",  # 2
    "V",  # 3
    "7",  # 4
    "B",  # 5
    "L",  # 6
    "0",  # 7
    "R",  # 8
    "I",  # 9
    "3",  # 10
    "F",  # 11
    "P",  # 12
    "4",  # 13
    "S",  # 14
    "U",  # 15
    "A",  # 16
    "X",  # 17
    "2",  # 18
    "E",  # 19
    "8",  # 20
    "O",  # 21
    "9",  # 22
    "G",  # 23
    "K",  # 24
    "5",  # 25
    "W",  # 26
    "C",  # 27
    "Q",  # 28
    "6",  # 29
    "J",  # 30
    "Y",  # 31
    ".",  # 32
    "D",  # 33
    "T",  # 34
    "Z",  # 35
    "M",  # 36
]


# Menu functions
def menu_prompt() -> str:
    """Print menu and get user input."""
    # print menu options using escape characters
    print("\t---Main menu---\nEnter E for Encryption\nEnter D for Decryption\nEnter X to Quit")

    # intermediate variable for valid options
    valid = ("e", "d", "x")
    # get choice from user, lowercase it, and strip leading/trailing whitespace
    choice: str = input("Please make a selection: ").strip().lower()
    # check if the choice is not in the tuple of valid options
    if choice not in valid:
        # if not in the tuple, raise ValueError with custom message
        invalid = "Invalid menu choice, please try again"
        raise ValueError(invalid)

    # return choice if valid
    return choice


# Function to encrypt text
def encrypt() -> str:
    """Encrypt the input text."""
    # get input
    plaintext_input: str = input("Please enter: ")
    # check for empty input
    if not plaintext_input:
        # if empty raise ValueError with custom message
        empty = "Input can't be empty"
        raise ValueError(empty)

    # encrypt text using helper function
    return parse_text(plaintext_input, encrypted=False)


# Function to decrypt text
def decrypt() -> str:
    """Decrypt the input text."""
    # get input
    encrypted_input: str = input("Please enter: ")
    # check for empty input
    if not encrypted_input:
        # if empty raise ValueError with custom message
        empty = "Input can't be empty"
        raise ValueError(empty)

    # decrypt text using helper function
    return parse_text(encrypted_input, encrypted=True)


# Helper function to parse text and encrypt or decrypt it
def parse_text(text: str, *, encrypted: bool) -> str:
    """Parse the text and encrypt or decrypt it."""
    # empty list to store parsed characters
    parsed_list: list[str] = []
    # go through each char in plaintext
    for char in text:
        # lookup index of char in map
        # use that index in array notation in KEY_MAP
        # append KEY_MAP[idx] to new list
        # if alpha and the upper char isnt in our cipher maps
        if char and char.upper() not in ALPHANUM_MAP:
            # append char as is
            parsed_list.append(char)
            # skip to next char
            continue

        if encrypted:
            # treat alpha different because case
            # if char is alpha use the uppercase version to check the list else use as is
            idx: int = KEY_MAP.index(char.upper()) if char.isalpha() else KEY_MAP.index(char)
            parsed_char: str = ALPHANUM_MAP[idx]
        else:
            # do the opposite of above
            idx = ALPHANUM_MAP.index(char.upper()) if char.isalpha() else ALPHANUM_MAP.index(char)
            parsed_char = KEY_MAP[idx]
        # append the parsed character to the list
        append_to_list(char, parsed_char, parsed_list)

    # return joined list
    return "".join(parsed_list)


# Helper function to append the parsed character to the list
def append_to_list(char: str, parsed_char: str, chars: list[str]) -> None:
    """Append the parsed character to the list."""
    if char.isupper():
        chars.append(parsed_char.upper())
    elif char.islower():
        chars.append(parsed_char.lower())
    else:
        chars.append(parsed_char)


def main() -> None:
    """Print substitution cipher program menu and get user input."""
    print(
        "┌------------------------------┐\n"
        "│ Substitution Cipher Program  │\n"
        "└------------------------------┘",
    )

    menu_choice = ""
    # loops until user picks x
    while menu_choice != "x":
        # try because menu_prompt can raise ValueError
        try:
            # get user input from menu_prompt()
            menu_choice: str = menu_prompt()

        # catch ValueError from menu_prompt()
        except ValueError as e:
            # print error
            print(e)
            # skip the rest of the loop and get next input
            continue

        # try because encrypt() and decrypt() can raise ValueError
        try:
            # call encrypt or decrypt based on user input
            if menu_choice == "e":
                # call encrypt and store result
                encrypted: str = encrypt()
                # print result
                print(encrypted)
            elif menu_choice == "d":
                # call decrypt and store result
                plaintext: str = decrypt()
                # print plaintext
                print(plaintext)
            elif menu_choice == "x":
                # print quit message
                print("Quitting...")
                # return
                return

        # catch ValueError from encrypt() and decrypt() functions
        except ValueError as e:
            # print error
            print(e)


main()
