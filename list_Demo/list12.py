def key_value(val):
    return val[2:3]
my_list=[(12,34,56,87),(32,54,76,76,89,98)]
my_list.sort(key=key_value)
print(my_list)