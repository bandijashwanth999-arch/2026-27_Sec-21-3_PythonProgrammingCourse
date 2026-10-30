#Unit-2A_Task-6_Smallest_of_Three_Nested_If.py
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3= int(input("Enter third number: "))
if number1 <= number2:
    if number1 <= number3:
        smallest = number1
    else:
        smallest = number3
else:
    if number2 <= number3:
        smallest = number2
    else:
        smallest = number3

print(f"Smallest = {smallest} (among {number1}, {number2}, {number3})")