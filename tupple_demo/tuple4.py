def my_tuple(a, b, c, d):
    return a + b + c + d


my_tuple1 = (1, 2, 3, 4)
x = my_tuple(*my_tuple1)
print(x)
