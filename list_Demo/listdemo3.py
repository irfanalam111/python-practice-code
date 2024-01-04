mylist = []
for x in range(1, 5):
    a = int(input("enter input for list: "))
    mylist.append(a)
print("list is:", mylist)
sum = 0
for x in mylist:
    print(x)
    sum += x
print(sum)
