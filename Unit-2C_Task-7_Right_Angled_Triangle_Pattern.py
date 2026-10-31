n = int(input("Enter number of rows: "))
s = input("Enter symbol: ")

for i in range(1, n+1):
    for j in range(i):
        print(s, end=" ")
    print()