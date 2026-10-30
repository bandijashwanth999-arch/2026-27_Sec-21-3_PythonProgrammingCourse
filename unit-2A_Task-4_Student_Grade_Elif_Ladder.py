marks=int(input("enter the total number of marks out of 100:"))
if marks>=90:
   print(f"grade:A(marks={marks})")
elif marks>=80:
    print(f"grade:B(marks={marks})")
elif marks>=70:
    print(f"grade:C(marks={marks})")
else:
    print(f"grade:D(marks={marks})")