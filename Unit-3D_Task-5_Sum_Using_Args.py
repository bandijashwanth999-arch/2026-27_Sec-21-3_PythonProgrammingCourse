def sum_values(*args):
    total = 0
    for value in args:
        total += value
    return total
print(sum_values(4, 5, 6))
print(sum_values(50, 70, 20, 50))