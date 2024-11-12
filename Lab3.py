import math #imports the math functionality to use math functions such as power and logarithm

#initialize variables
operand1 = 0 #initiates the variable for the first inputted operand
operand2 = 0 #initiates the variable for the second inputted operand
result = 0 #initiates the variable for the result of every math problem the user has the program solve
resultTotal = 0 #initiates the variable for adding all the results from every math problem the user has the program solve
calcNum = 0 #initiates the variable for the number of calculations completed by the program

#creates a function that displays the menu of options the user can choose from
def calc_menu():
    print("Calculator Menu")
    print("---------------")
    print("0. Exit Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print("7. Display Average")
    print("")

#creates a function to convert all inputted operands to numbers that can be operated with
def get_operand(prompt):
    value = input(prompt)
    if value.upper() == "RESULT": #checks if the inputted value is RESULT, in which the result of the previous calculation is used as one or both of the operands in the new calculation
        return result
    return float(value)

#starts the program/calculator
print(f"Current Result: {result:.1f}")
print("")
calc_menu()
menuSelect = int(input("Enter Menu Selection: "))

#while loop so the program keeps running until the user chooses to end the program
quit_game = False
while not quit_game:
    if menuSelect == 0: #quits the program if option 0 is selected
        print("Thanks for using this calculator. Goodbye!")
        quit()
    elif menuSelect == 1: #completes addition calculation with the two numbers the user inputs if option 1 is selected
        operand1 = get_operand("Enter first operand: ")
        operand2 = get_operand("Enter second operand: ")
        result = operand1 + operand2
        print(f"Current Result: {result}")
        calcNum += 1
        resultTotal += result
        print("")
        calc_menu()
        menuSelect = int(input("Enter Menu Selection: "))
    elif menuSelect == 2: #completes subtraction calculation with the two numbers the user inputs if option 2 is selected
        operand1 = get_operand("Enter first operand: ")
        operand2 = get_operand("Enter second operand: ")
        result = operand1 - operand2
        print(f"Current Result: {result}")
        calcNum += 1
        resultTotal += result
        print("")
        calc_menu()
        menuSelect = int(input("Enter Menu Selection: "))
    elif menuSelect == 3: #completes multiplication calculation with the two numbers the user inputs if option 3 is selected
        operand1 = get_operand("Enter first operand: ")
        operand2 = get_operand("Enter second operand: ")
        result = operand1 * operand2
        print(f"Current Result: {result}")
        calcNum += 1
        resultTotal += result
        print("")
        calc_menu()
        menuSelect = int(input("Enter Menu Selection: "))
    elif menuSelect == 4: #completes division calculation with the two numbers the user inputs if option 4 is selected
        operand1 = get_operand("Enter first operand: ")
        operand2 = get_operand("Enter second operand: ")
        if operand2 == 0: #checks if the division denominator is zero, and displays an error message because you cant divide by zero
            print("Error: invalid input!")
            print("")
            menuSelect = int(input("Enter Menu Selection: "))
        else: #continues with the division given that you are not trying to divide by zero
            result = operand1 / operand2
            print(f"Current Result: {result}")
            calcNum += 1
            resultTotal += result
            print("")
            calc_menu()
            menuSelect = int(input("Enter Menu Selection: "))
    elif menuSelect == 5: #completes exponentiation calculation with the two numbers the user inputs if option 5 is selected
        operand1 = get_operand("Enter first operand: ")
        operand2 = get_operand("Enter second operand: ")
        if operand1 == 0 and operand2 == 0: #makes sure the user is not trying to raise zero to the power of zero because this is not possible displays an error message if the user does try
            print("Error: invalid input!")
        else: #completes the exponentiation calculation given that the user is not raising zero to the power of zero
            result = math.pow(operand1, operand2)
            print(f"Current Result: {result}")
            calcNum += 1
            resultTotal += result
            print("")
            calc_menu()
            menuSelect = int(input("Enter Menu Selection: "))
    elif menuSelect == 6: #completes logarithm calculation with the two numbers the user inputs if option 6 is selected
        operand1 = get_operand("Enter first operand: ")
        operand2 = get_operand("Enter second operand: ")
        if operand1 > 0: #makes sure the number you are trying to take the logarithm of is greater than zero because you cant take the logarithm of a number that is zero or negative no matter the base
            result = math.log(operand2, operand1)
            print(f"Current Result: {result}")
            calcNum += 1
            resultTotal += result
            print("")
            calc_menu()
            menuSelect = int(input("Enter Menu Selection: "))
        else: #displays an error message if you try to take the logarithm of a negative number or zero because this is not possible
            print("Error: invalid input!")
            print("")
            menuSelect = int(input("Enter Menu Selection: "))
    elif menuSelect == 7: #displays the average of all the calculations that the program has completed so far if option 7 is selected
        if calcNum > 0: #makes sure you have had the program complete at least 1 calculation before calculating the average of all the calculations made so far
            print(f"Sum of calculations: {resultTotal}")
            print(f"Number of calculations: {calcNum}")
            print(f"Average of calculations: {resultTotal/calcNum:.2f}")
            print("")
            menuSelect = int(input("Enter Menu Selection: "))
        else: #displays an error message if you try to calculate the average of all calculations made so far if you haven't had the program calculate anything yet because you cannot divide by the zero number of calculations made so far
            print("Error: No calculations yet to average!")
            print("")
            menuSelect = int(input("Enter Menu Selection: "))
    else: #displays an error message if the user tries to choose an option that is not part of the menu displayed
        print("Error: Invalid selection!")
        print("")
        menuSelect = int(input("Enter Menu Selection: "))