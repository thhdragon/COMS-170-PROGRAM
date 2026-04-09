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


def menu_prompt() -> str | None:
    print("Main menu")
    print("Enter E for Encryption")
    print("Enter D for Decryption")
    print("Enter X to Quit")

    valid = ("e", "d", "x")
    choice: str = input("Please make a selection: ").strip().lower()
    if choice not in valid:
        return None
    return choice


def encrypt() -> str:
    # get input
    plaintext_input: str = input("Please enter: ")
    # encrypt text
    return parse_text(plaintext_input, encrypted=False)


def decrypt() -> str:
    # get input
    encrypted_input: str = input("Please enter: ")
    # encrypt text
    return parse_text(encrypted_input, encrypted=True)


def parse_text(text: str, *, encrypted: bool) -> str:
    # go through each char in plaintext
    parsed_list: list[str] = []
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
            idx = KEY_MAP.index(char.upper()) if char.isalpha() else KEY_MAP.index(char)
            parsed_char: str = ALPHANUM_MAP[idx]
        else:
            # do the reverse from above
            idx = ALPHANUM_MAP.index(char.upper()) if char.isalpha() else ALPHANUM_MAP.index(char)
            parsed_char: str = KEY_MAP[idx]

        append_to_list(char, parsed_char, parsed_list)

    return "".join(parsed_list)


def append_to_list(char: str, parsed_char: str, chars: list[str]) -> None:
    is_upper = char.isupper()
    is_lower = char.islower()
    if is_upper:
        chars.append(parsed_char.upper())
    elif is_lower:
        chars.append(parsed_char.lower())
    else:
        chars.append(parsed_char)


def main() -> None:
    print("Substitution Cipher Program")
    while True:
        menu_choice: str | None = menu_prompt()
        if menu_choice is None:
            continue
        if menu_choice == "e":
            encrypted: str = encrypt()
            print(encrypted)
        if menu_choice == "d":
            plaintext: str = decrypt()
            print(plaintext)
        if menu_choice == "x":
            print("quit")
            break


main()
