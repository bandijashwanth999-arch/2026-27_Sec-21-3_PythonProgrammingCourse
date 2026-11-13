def r(length,breadth):
    area = length * breadth
    perimeter = 2 *(length+breadth)
    return area, perimeter
length = 499
breadth= 987
area, perimeter = r(length, breadth)
print("area:",area)
print("perimeter:",perimeter)