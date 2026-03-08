Pseudocode containing:
a. A main function that displays a menu of choices. Menu choices are:
C: Calculate Interest
D: Display Interest Information
X: Exit application
The menu will display until the user enters X to exit the application.
b. A function named DisplayInfo that displays the interest calculation formula as shown below.
This function accepts zero arguments and does not return any values.
The simple interest formula is:
Interest = Principal x Rate x Time
The Principal is the amount of money invested.
The Rate is the annual interest rate the money will earn.
The Time is the number of years the money will be invested for.
c.
A function named TotalAccount that asks how much money the user will be investing, the
interest rate entered as a percentage (e.g., enters 6 for 6% interest), and the number of years the
money will be invested. This function accepts zero arguments and returns two (2) values. The
values returned are the amount of interest earned based off the simple interest calculation and
the total amount in the account based off starting principal and the amount of interest earned.
d.
A function named CalcInterest. This function accepts three (3) parameters named principal, rate,
and time and returns one (1) value. The value returned is the amount of interest made based on
those 3 values as calculated with the simple interest formula (I = Prt).

`# function CalcInterest takes principal: int, rate: int, time: int as arguments and returns the interest: float`
   `# calculate interest using the formula: interest = principal * rate * time / 100`
   `# divide by 100 because the input takes the rate as a whole number instead of a decimal`
   `# return the interest`

`# function TotalAccount takes no arguments and returns the interest and total account value`
   `# print the input instructions header`
   `# use input() to get the principal, rate, and time`
   `# cast the input to int`
   `# calculate interest by passing the principal, rate, and time to CalcInterest`
   `# add interest to principal to get total`
   `# return the interest and total account value`

`# function DisplayInfo takes no arguments and returns nothing`  
   `# print the information about the simple interest formula`

`# function main takes no arguments and returns nothing`
   `# prime the loop by initializing menu_choice to an empty string so it doesn't fail on first iteration`
   `# loop until user enters x`
       `# print menu intro message`
       `# get user input for menu choice. cast it to lower so we don't have to compare both cases`
       `# validate input against menu options by checking if it is in c d or x`
           `# if menu_choice is "c"`
               `# call TotalAccount(), store results into interest and total`
               `# print the interest and total account value`
           `# if menu_choice is "d" then display information`
               `# call DisplayInfo()`
           `# if menu_choice is "x"`
               `# print quit message`
       `# if menu_choice is not "c", "d", or "x"`
           `# print error message`

# IPO charts

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
