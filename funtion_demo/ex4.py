def outer_(a,b):
    square= a**2
    def inner_(a,b):
        return a+b
    add=inner_(a,b)
    return add+5
result=outer_(5,10)
print(result)
