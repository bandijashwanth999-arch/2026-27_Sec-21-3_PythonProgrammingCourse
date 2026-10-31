num = int(input("Enter a number: "))

original = num
reversed_number = 0

while num > 0:
    digit = num % 10
    reversed_number = reversed_number * 10 + digit
    num = num // 10

print("Reverse of", original, "is", reversed_number)