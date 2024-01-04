from random import *
import os
pas=input("enter your password")
pwd=['a','b','c','d','e','f','g','h',1,2,3,4,5,6,7,8,9]
pw=""
while(pw!=pas):

     for i in  range(len(pas)):

          gwss_paa=pwd[randint(0,9)]
          pw=str(gwss_paa)+str(pw)
          print(pw)
          print("cracking password ! please wait.....")
          os.system("cls")
print("your password is : ",pw)
