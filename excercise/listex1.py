# my_list=[12,34,56,76,8]
# mul=1
# for i in my_list:
#     mul*=i
#     print(mul)
# my_list=[12,34,56,76,8]
# print(max(my_list))
# my_list=[12,34,56,76,8]
# print(min(my_list))
#
# for i in range(0,11):
#     print(i)
# row=5
# for i in range(1, row+1):
#     for j in range (1,i+1):
#         print(j,end=' ')
#     print("")
my_list=[]
a=int(input("enter your number : "))
for i in range(1,a):
    my_list.append(i)
    print(my_list)
    print(sum(my_list))
