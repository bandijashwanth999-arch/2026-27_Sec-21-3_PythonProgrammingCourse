a=float(input("enter the angle A:"))
b=float(input("enter the angle B:"))
c=float(input("enter the angle C:"))
if a>0 and b>0 and c>0 and a+b+c==180:
    print(f"valid triangle(angle={a},{b},{c})")
else:
    print(f"valid triangle(angle={a},{b},{c},)")