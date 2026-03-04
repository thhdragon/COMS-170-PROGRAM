function CalcTotal (input: no input) (output: two float values or None on error)
    initialize variables prices and idx outside the loop so they stay alive after the loop ends
    start a try block because opening a file can error on a missing or bad file. converting a string to a float will also error on non numeric characters
        use pythons with statement to open the file and return a handle to the file object. with will automate closing the file even if the program crashes
        if no/bad/corrupt file is found, jump to except FileNotFoundErrors
            start a for loop to go through each line in the file
                use rstrip() to strip the \n from the end of the line store it in line_cleaned
                use float() to convert the line_cleaned to a float and store it in price
                if converting to a float fails (see above), jump to except ValueError
                increment idx by 1. idx = idx + 1
                add the price to the prices variable. prices = prices + price

    if opening the file fails (see above), print the error message and return None
    use None to orchestrate error handling
    if converting to a float fails (see above), print the error message and return None
    use None to orchestrate error handling
    if nothing fails, return the prices and the average (average = prices / idx)

function DisplayCardSales (input: no input) (output: None)
    initialize index variable (idx) outside the loop so it stays alive after the loop ends
    start a try block because opening a file can error on a missing or bad file. converting a string to a float will also error on non numeric characters
        use pythons with statement to open the file and return a handle to the file object. with will automate closing the file even if the program crashes
            start a for loop to go through each line in the file
                use rstrip() to strip the \n from the end of the line store it in line_cleaned
                use float() to convert the line_cleaned to a float and store it in price
                increment idx by 1. idx = idx + 1
                print the index and price

        if opening the file fails (see above), print the error message and return None
        implicit None subtly hinting the return value has no purpose
        if converting to a float fails (see above), print the error message and return None
        implicit None subtly hinting the return value has no purpose

function main (input: no input) (output: None)
    initialize menu_selection variable
    start a while loop to keep the menu open until the user enters x
    selection != x
        print the menu
"           **********************
            *Pokemon Card Sales*
            **********************
            D: Display Sales
            C: Calculate Total and Average
            X: Exit application"
        use pythons input function to get the menu selection and store it in menu_selection
        use pythons lower function to convert the menu_selection to lowercase
        lowercase makes it case insensitive
        if the menu_selection is not c, d, or x
            print bad input back to user.
            use continue to shortcut back to the top of the loop (retry)
        if the menu_selection is c
        call the function CalcTotal and store its reply in variable response
            check if the response is None
                print a message and continue.
                same as above use continue to shortcut back to the start (retry)
            now that the response is checked to not be empty unpack it into total and average variables
            print the results to the user. eg..
"           Total Sales:  $151.31
            Average Sale: $2.80"
        if the menu_selection is d
            call the function DisplayCardSales
