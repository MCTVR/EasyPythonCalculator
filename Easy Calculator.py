#calculator
#introduction to calculator, and user input

print("Welcome to the calculator!")
print("+ for addition, - for subtraction, x for multiplication, / for division")
print("Type your first number below, e.g. 1")
x = float(input())
print("Type your operator below, e.g. +")
operator = input()
print("Type your second number, e.g. 2")
y = float(input())
print("Thank you, thecalculator is calculating!")

#def +-*/

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

#print results

if operator == "+":
    print(add(x, y))
if operator == "-":
    print(sub(x, y))
if operator == "*" or operator == "x":
    print(mul(x, y))
if operator == "/":
    print(div(x, y))

#ending

print("Run the code again to calculate again.")

#Made by Master Creeper




