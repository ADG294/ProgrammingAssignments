from functools import reduce
# This program creates a list of user input with expenses
# and then uses a loop to append each expense to the list.
# After, this program uses the reduce function from the functools
# package that adds the total expenses and calculates
# the min and max expenses then displays the expenses.

# Create an add function
def add(x, y):

    return x + y

# Create the main function
def main():

    #  Create an empty list and variables that are null
    ex_list = []

    ex_result = 0

    r_min = 0

    r_max = 0

    # Create a while loop
    while True:

        # Have user input the name of their expense.
        u_in = input('Enter your expense: ')

        # Create a condition that if enter is pressed
        # without input program resolves and exits.
        if len(u_in) == 0:

            break

        # Have user enter the amount of the expense.
        u_amount = int(input("Enter amount: "))

        # Append amount to ex_list
        ex_list.append(u_amount)

        # Use reduce method to apply our add function to ex_list.
        ex_result = reduce(add, ex_list)

        # Use reduce method to create a lambda function
        # that finds the lowest expense from the list.
        r_min = reduce(lambda x, y: x if x < y else y, ex_list)

        # Use reduce method to create a lambda function
        # that finds the highest expense from the list.
        r_max = reduce(lambda x, y: x if x > y else y, ex_list)

    # Print all of our expenses
    print(f'Total Expenses: {ex_result}\nLowest Expense: {r_min}\nHighest Expense: {r_max}')

# Execute main function
main()


