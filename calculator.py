# basic calculator created by Steven Cowley

# variables
running = True

# functions
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if x == 0 or y == 0:
        print("sorry! cannot divide by 0")
        return None
    else:
        return x / y


# main program (user interactions)
while running:
    userAns = input("Welcome to my calculator, what function would you like to perform\n1.Add\n2.subtract\n3.multiply\n4.divide\n")

    # program ends if user enters q
    if userAns == 'q' or userAns == 'Q':
        running = False
    elif userAns in {'1', '2', '3', '4'}:

        # x and y are floats because we will run into less logic errors
        x = float(input("please enter the first number: "))
        y = float(input("please enter the second number: "))

        # if 1 through 4 is pressed the corresponding function is executed
        operations = {
            '1': add,
            '2': subtract,
            '3': multiply,
            '4': divide
        }

        # result is eaual to the operation that matches the choice within the operations array
        # x and y are taken in as perameters for the corresponding method
        result = operations[userAns](x, y)
        
        # checks to see if the result is not empty
        # prints the result to the user
        if result is not None:
            print(f"Result is: {result}")
    else:
        # if the user enters an invalid entry loop back to the main menu
        print("invalid input please enter 1, 2, 3, 4 or q to quit")