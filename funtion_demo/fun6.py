def grocery(item, price):
    return item, price


x = grocery(item="mango", price=456)
y = grocery(price=456, item="piza")
print(x, y)
