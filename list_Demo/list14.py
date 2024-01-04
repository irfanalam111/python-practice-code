def value(a):
    return a[-1]

my_list=[(1,6),(3,8),(8,7)]
my_list.sort(key=value)
print(my_list)
