#introduction to calculator, and user input

print("Welcome to the calculator!")
print("+ for addition, - for subtraction, x for multiplication, / for division")

"""
while loop and print ans
"""
while True:

    print("Type your first number below, e.g. 1")
    x = float(input())
    print("Type your operator below, e.g. +, times, subtract")
    operator = input()
    print("Type your second number, e.g. 2")
    y = float(input())
    print("Thank you, the calculator is calculating!")

#print results
    if operator == "+" or operator == "plus" or operator == "add":
            print("The answer is =", x + y)
    if operator == "-" or operator == "minus" or operator == "subtract":
            print("The answer is =", x - y)
    if operator == "*" or operator == "x" or operator == "times" or operator == "multiply":
            print("The answer is =", x * y)
    if operator == "/" or operator == "divide":
            print("The answer is =", x / y)

#Made by Master Creeper




