def key_value(val):
    return val[0]
my_list=[(1,11),(2,3),(4,66)]
my_list.sort(key=key_value)
print(my_list)