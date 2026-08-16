# # Given the list of roll numbers: [101, 105, 102, 101, 108, 105, 110]. print all unique roll number in a list
# #sol.
# rollNumbers = [101, 105, 102, 101, 108, 105, 110]
# print (list(set(rollNumbers)))

# """
# Given Employee records in the form of a list of tuples where each tuple contains:
# (Employee ID, Employee Name, Salary)
# Example - [
#     (101, "Alice", 50000),
#     (102, "Bob", 65000),
#     (103, "Charlie", 45000)
# ]
# Ask user to enter Employee ID & search it inside records.
# """
# #sol.
# employees = [
#     (101, "Alice", 50000),
#     (102, "Bob", 65000),
#     (103, "Charlie", 45000)
# ]

# def dataFormatter (employee):
#     (id, name, salary) = employee
#     print(f"""
# Employee ID: {id}
# Name: {name}
# Salary: {salary}
# """)

# id = int(input("Enter The ID: "))


# def showEmployee():
#     isFound = False
#     for employee in employees:
#         if id == employee[0]:
#             dataFormatter(employee)
#             isFound = True
#     if not isFound:
#         print("404: Employee not Found.")

# showEmployee()

#  # Write a Function (WAF) to check if a number is odd or even.
# #sol.
# numb = int(input("Enter the number: "))
# def isWhat(num):
#     print (f"{num} is {"an even" if num%2==0 else "a odd"} number.")

# isWhat(numb)

# # WAF to count the number of vowels in a string
# # sol.
# def countVowelsButBitAdvance (str):
#     vowels = ("A", "E", "I", "O", "U")
#     vowelCounter = {"A":0, "E":0, "I":0, "O":0, "U":0}
#     totalCount =0

#     try:
#         CapsOn= str.upper()
#     except Exception as e:
#         print (f"Error Occured: {e}")
#         return -1

#     for char in CapsOn:
#         if char in vowels:
#             vowelCounter[char] +=1

#     for key in vowelCounter:
#         totalCount += vowelCounter[key]

#     return {"Count":totalCount, "Reps": vowelCounter}

# strin = input("Enter your String: ")
# print(countVowelsButBitAdvance(strin)["Count"])
# print(countVowelsButBitAdvance(strin)["Reps"])


def isPrime (num):
    return True if num/(num/4) else False

for i in range(7):
    print(isPrime(int(input("Enter Your Number: "))))




