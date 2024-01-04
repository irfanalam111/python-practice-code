import sys
a=dir(sys)
for i in  a:
    print(i)
b=sys.winver
c=sys.stdlib_module_names
for i in c:
    with open('password.txt','w') as file:
        file.write('\n')
