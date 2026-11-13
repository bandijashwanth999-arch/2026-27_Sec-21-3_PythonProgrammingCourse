def total_and_average(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

m1=float(input("enter your marks1:"))
m2=float(input("enter your marks2:"))
m3=float(input("enter your marks3:"))
total, average = total_and_average(m1, m2, m3)
print("Total:", total)
print("Average:", average)