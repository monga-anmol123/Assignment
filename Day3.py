# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:46:33 2020

@author: Anmol Monga
"""
""" Question 1"""

x=int(input())

if x<1000 :
    print("land the plane")
elif x>1000 and x<=5000 :
    print("come down to 1000ft")
else :
    print("go around and trylater")


"""Question2 """
    
for i in range(2,200):
    b=1;
    for j in range(2,i-1):
        if(i%j==0):
            b=0
            break
        
    if(b==1):
        print(i)
            