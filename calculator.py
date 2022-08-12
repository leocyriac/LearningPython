def add(a, b):
    """
    This function accepts two integer values and returns the sum of them.
    :param a: first number to add - Should be integer
    :param b: second number to add - Should be integer
    :return: Returns the sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    This function accepts two integer values and returns the difference of a - b
    :param a: First number - Should be integer
    :param b: Second number - Should be integer
    :return: Returns the difference a - b
    """
    return a - b


def display_options():
    """
    This function displays calculation options to the user so that,
    the user can select one from them using the number corresponding to it.
    :return: This returns nothing
    """

    print("Choose an option from the following:")
    print("(1) Add(+)")
    print("(2) Subtract(-)")
    print("(3) Multiply(*)")
    print("(4) Divide(/)")
    print("(5) Find Remainder(%)")
    print("(6) Find Quotient (//) ")
    print("(7) Find Square of a number (**)")


display_options()

option = int(input("Option selected : "))

if option == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Output is :")
    print(add(num1, num2))
elif option == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Output is :")
    print(subtract(num1, num2))
