value = 0
temp_total = 0
operatores = ("A", "S", "M", "D", "P", "H") #using tuple because it is faster to perform opertarions on immutable data types.


# user will first select operation from Add, subtract, multiply, devide, and power. after results. user will get prompt to clear, end, or continue by selecting the operator.
def takeInput():
    while True:
        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            return [num1, num2]
        except Exception:
            print("Please Enter Correct Number.")
            continue

def help():
    print ("""
Actions are listed Below:
Type:
    Q for Quitting
    A for Addition
    S for Subtraction
    M for Multiplication
    D for Division
    P for Powder 
""")
    return 1

while True:
    operation = input("Your Action: ").capitalize()
    if operation == "Q":
        break
    elif operation == "H":
        help()

    elif operation in operatores:
        (num1, num2)= takeInput()
        if operation == "A":
            print (num1+num2)
        elif operation == "S":
            print (num1-num2)
        elif operation == "M":
            print (num1*num2)
        elif operation == "D":
            try:
                print (num1/num2)
            except ZeroDivisionError:
                print ("Can't be divided by Zero.")
        elif operation == "P":
            print(num1**num2)
        else: 
            print("Unspecified Shit.")

    else: 
        print("Wrong Operator Selected. Press h for help.")


