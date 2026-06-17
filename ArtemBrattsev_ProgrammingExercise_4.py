# Name: Artem Brattsev
# Course: COP 2373
# Programming Exercise 3(4 if counting debug assignment) - Monthly Expenses

from functools import reduce # Import the reduce function.

# This class stores expenses and performs calculations.
class ExpenseAnalyzer:

    def __init__(self):  # Create an empty list to store expenses.
        self.expenses = []

    def add_expense(self, expense_type, amount): # Add an expense type and amount to the list.
        self.expenses.append((expense_type, amount))

    def get_total_expense(self): # Calculate the total of all expenses using reduce
        return reduce(lambda total, expense: total + expense[1], self.expenses, 0)

    def get_highest_expense(self): # Find the expense with the highest amount
        return reduce(
            lambda highest, current: current if current[1] > highest[1] else highest,
            self.expenses
        )

    def get_lowest_expense(self): # Find the expense with the lowest amount
        return reduce(
            lambda lowest, current: current if current[1] < lowest[1] else lowest,
            self.expenses
        )


def main():

    analyzer = ExpenseAnalyzer() # Create an ExpenseAnalyzer object.

    number_of_expenses = int(input('How many monthly expenses would you like to enter? ')) # Ask the user how many expenses they want to enter

    for count in range(number_of_expenses): # Loop through number of expenses entered by user

        print()

        expense_type = input('Enter the expense type: ') # Ask for the type of expense
        amount = float(input('Enter the expense amount: $')) # Ask for the expense amount

        analyzer.add_expense(expense_type, amount) # Add expense to the list

    total = analyzer.get_total_expense() # total expense amount
    highest = analyzer.get_highest_expense() # highest/biggest value
    lowest = analyzer.get_lowest_expense() # lowest/smallest value

    print()
    print('Expense Summary') # display results
    print('-------------------')
    print('Total Expenses: $', total)
    print('Highest Expense:', highest[0], '- $', highest[1])
    print('Lowest Expense:', lowest[0], '- $', lowest[1])


main() # runs program
