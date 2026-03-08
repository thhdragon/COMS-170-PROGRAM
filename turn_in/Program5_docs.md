# Pseudocode for Program 5

```py
# function CalcInterest takes principal: int, rate: int, time: int as arguments and returns the interest: float
   # calculate interest using the formula: interest = principal * rate * time / 100
   # divide by 100 because the input takes the rate as a whole number instead of a decimal
   # return the interest

# function TotalAccount takes no arguments and returns the interest and total account value
   # print the input instructions header
   # ask how much money the user will be investing
   # ask the interest rate entered as a percentage (e.g., enters 6 for 6% interest)
   # ask the number of years the money will be invested
   # cast the input to int
   # calculate interest by passing the principal, rate, and time to CalcInterest
   # add interest to principal to get total
   # return the interest and total account value

# function DisplayInfo takes no arguments and returns nothing  
   # print the simple interest formula: Interest = Principal x Rate x Time
   # print The Principal is the amount of money invested.
   # print The Rate is the annual interest rate the money will earn.
   # print The Time is the number of years the money will be invested for.

# function main takes no arguments and returns nothing
   # prime the loop by initializing menu_choice to an empty string so it doesn't fail on first iteration
   # loop until user enters x
       # print C: Calculate Interest
       # print D: Display Interest Information
       # print X: Exit application
       # get user input for menu choice. cast it to lower so we don't have to compare both cases
       # validate input against menu options by checking if it is in c d or x
           # if menu_choice is "c"
               # call TotalAccount(), store results into interest and total
               # print the interest and total account value
           # if menu_choice is "d" then display information
               # call DisplayInfo()
           # if menu_choice is "x"
               # print quit message
       # if menu_choice is not "c", "d", or "x"
           # print error message
```

## IPO charts

**CalcInterest:**

| Input | Processing | Output |
| ----- | ----- | ----- |
| principal, rate, years | (principal \* rate \* years) / 100 | interest |

**TotalAccount:**

| Input | Processing | Output |
| ----- | ----- | ----- |
| None | Prompt user for principal, rate, and years | interest, total\_account |
|  | Call CalcInterest with principal, rate, and years |  |
|  | Calculate total\_account from principal \+ interest |  |
|  | Return interest and total\_account |  |

**DisplayInfo:**

| Input | Processing | Output |
| ----- | ----- | ----- |
| None | Print info about the simple interest formula | None |

**main:**

| Input | Processing | Output |
| ----- | ----- | ----- |
| None | Loop until user enters "x" to exit | None |
|  | Prompt user for menu choice (c, d, x) |  |
|  | If "c", call TotalAccount and print interest and total account value |  |
|  | If "d", call DisplayInfo to show info about interest formula |  |
|  | If "x", print quit message and exit loop |  |
|  | If invalid input, print error message |  |
