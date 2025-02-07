def add(x, y):
    return x + y

def subtract(x, y):
    return x - y


def multi(x, y):
    return x * y


def divide(x, y):
    return x / y

print("Select one of the 4 options: \n")
print("1. Add \n")
print("2. Subtract \n")
print("3. Mulitply \n")
print("4. Divide \n") 

while True:

    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))
    choice = input("Type 1/2/3/4: ")

    if choice=="1": 
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice=="2":
        print(num1, "-", num2, "=", subtract(num1,num2))

    elif choice=="3":
        print(num1, "*", num2, "=", multi(num1,num2))

    elif choice=="4":
        print(num1, "%", num2, "=", divide(num1,num2))
        
    con = input("Want to do more Math? yes/no: ")

    if con == "no":
        break 
    else:
        print("")

