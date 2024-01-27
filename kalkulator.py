def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

number1 = float(input("Enter the first number and press enter: "))
number2 = float(input("Enter the second number and press enter: "))

print("\nChoose the operation:")
print("1.---> Addition")
print("2.---> Subtraction")
print("3.---> Multiplication")
print("4.---> Division")

choice = input("\nChoose the operation number (1/2/3/4) and press enter: ")

if choice in ('1', '2', '3', '4'):
    if choice == '1':
        result = addition(number1, number2)
    elif choice == '2':
        result = subtraction(number1, number2)
    elif choice == '3':
        result = multiplication(number1, number2)
    elif choice == '4':
        result = division(number1, number2)
    print(f"\nResult: {result}")
else:
    print("Invalid operation choice.")
