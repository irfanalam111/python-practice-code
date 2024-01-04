def multiple(a, b):
    c = a + b
    d = a - b
    return c, d


first = int(input("enter first number: "))
sec = int(input("enter second number: "))
x = multiple(first, sec)
m, n = x
print(m)
print(n)
