import itertools
char='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$*'
pass_wd=8
for i in pass_wd:
    combination=itertools.product(char,repeat=i)
with open('password.txt','w') as file:
    for combination in combination:
        password="".join(combination)
        file.write(password +'\n')
print("password wordlist generated and save as 'passwords.txt'")