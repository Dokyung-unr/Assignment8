# Simple Expense Tracker

## project description
This is a simple python program to record daily expenses.

## Initial Version
The initial version has three menu options:
- Add an expense
- View expenses
- Exit the program

The program uses functions, loops, a list, and user input.

## AI Tool Used
Chatgpt and github copilot

## AI Assistance
I used AI to improve my expense tracker by adding price validation and a total expense calculation.

## New or modified features
- Added price validationi using try and except
- Prevented zero and negative prices
- Added a totla expense calculation
- Added a message when no expenses are recorded
- Added a check for empty item names

## evaluation of ai output
I reviewed the AI suggestions and modified the code to keep it simple.

## how to run the program
1. Open the project forder in VS Code.
2. Open the terminal.
3. Type: python3 main.py
4. Choose the option from the menu.

## Feature Development comparison
For this assignment, I added two features to my Expense Tracker program using different development approaches.
The first feature was Count Expenses, which displays the total number of recorded expenses.
The second feature was Most Expensive Expense, which identifies the purchase with the highest price. I used ChatGPT to generate the function and help integrate it into the program. The AI-generated code used a loop to compare the prices of recorded expenses.

But features worked during testing. I tested the empty expense list and a list containing Coffee and Lunch. However, when merging the branches, I encountered a conflict because both features used menu option 4. I resolved this by assigning different menu numbers to each feature and changing Exit to option 6.

The manual approach helped me understand the program structure more clearly, while the AI approach made implementation faster. Reviewing and testing both features helped me gain confidence in the final program.
