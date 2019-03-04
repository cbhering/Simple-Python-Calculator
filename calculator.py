#Simple Python 2 Calculator

print ("WELCOME TO BHERING CALCULATOR")

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

#Sum procedure
def add(x, y):
    return x + y

#Subtraction procedure
def subtraction(x, y):
    return x - y

#Multiplication procedure
def multiply(x, y):
    return x * y

#Division procedure
def division(x, y):
    return x / y

operation = raw_input("Select (+, -, *, /): ")

if operation == '+':
    print add(x, y)

if operation == '-':
    print subtraction(x, y)

if operation == '*':
    print multiply(x, y)

if operation == '/':
    print division(x, y)







