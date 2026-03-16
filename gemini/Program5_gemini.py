def display_info():
    """Prints information about the simple interest formula."""
    print("\n--- Simple Interest Formula ---")
    print("Simple Interest = (Principal * Rate * Time) / 100")
    print("\nWhere:")
    print("- Principal is the starting amount of money.")
    print("- Rate is the interest rate (entered as a whole number, e.g., 6 for 6%).")
    print("- Time is the number of time periods (usually years).")
    print("-------------------------------\n")


def calculate_interest():
    """Prompts the user for inputs and calculates simple interest."""
    print("\n--- Calculate Simple Interest ---")
    try:
        # Taking inputs as integers as requested
        principal = int(input("Enter the Principal amount: "))
        rate = int(input("Enter the Interest Rate (e.g., enter 6 for 6%): "))
        time = int(input("Enter the Time period: "))

        # Calculate interest
        interest = (principal * rate * time) / 100

        # Print results
        print("\n*** Results ***")
        print(f"Principal: ${principal}")
        print(f"Rate:      {rate}%")
        print(f"Time:      {time}")
        print(f"Calculated Simple Interest: ${interest:.2f}")
        print("***************\n")

    except ValueError:
        print("\n[Error] Invalid input. Please enter whole numbers (integers) only.\n")


def main():
    """Main program loop that displays the menu and handles user choices."""
    while True:
        print("===========================")
        print("   Simple Interest Menu    ")
        print("===========================")
        print(" [C] Calculate Interest")
        print(" [D] Display Formula Info")
        print(" [X] Exit")
        print("===========================")

        choice = input("Select an option (C, D, X): ").strip().upper()

        if choice == "C":
            calculate_interest()
        elif choice == "D":
            display_info()
        elif choice == "X":
            print("\nExiting the program. Goodbye!\n")
            break
        else:
            print("\n[Error] Invalid option. Please choose C, D, or X.\n")


if __name__ == "__main__":
    main()
