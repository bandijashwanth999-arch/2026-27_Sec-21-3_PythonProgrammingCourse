n = int(input("Enter how many numbers: "))

largest = 0

for i in range(n):
    num = int(input("Enter a number: "))

    if num > largest:
        largest = num

print("Largest number =", largest)