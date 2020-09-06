# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 16:25:48 2020

@author: Anmol Monga
"""

list=[1,2,3,4,5]
list.append(1)
print(list)

p=list.count(1)
print(p)

m=list.index(2)
print(m)

list.reverse()
print(list)

list.sort()
print(list)


"""DICTIONARY
"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car) 

x = car.keys()
print(x)

car.update({"color": "White"})
print(car) 

x = car.get("model")
print(x) 

x = car.copy()
print(x) 

"""SETS"""
fruits = {"apple", "banana", "cherry"}

fruits.add("orange")
print(fruits) 


x = fruits.copy()
print(x) 

y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z) 

z = x.union(y)
print(z)

z = x.intersection(y)
print(z) 

fruits.clear()
print(fruits) 


"""Strings"""

txt = "hello, and welcome to my world."

x = txt.capitalize()
print (x) 

x = txt.casefold()
print(x) 

x = txt.replace("hello", "apples")
print(x) 

x = txt.upper()
print(x) 

x = txt.isalpha()
print(x)