num = int(input("Enter a number: "))
original = num
digit_count = 0
if num == 0:
    digit_count = 1
else:
    while num > 0:
        digit_count = digit_count + 1
        num = num // 10
print("Number of digits in", original, "is", digit_count)