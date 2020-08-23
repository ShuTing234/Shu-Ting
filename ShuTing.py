# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:20:18 2020

@author: TANST
"""

#---------------------Question 1----------------------------
import numpy as py
def calc(m,n, inp):
    numbers = []
    if m==1:
        numbers= [1]*n
        
    elif n==1:
        numbers= list(range(1, m+1))
        
    elif m ==2 and n== 2:
        if inp == 4:
            numbers = [1,1,2]
        else:
            numbers = [1,2,2]
      
    else: 
        # numbersD= calc(m-1, n, inp-m) +[ m]
        if calc(m-1, n, inp-m) +[ m] == inp: #move up
            numbers= calc(m-1, n, inp-m) +[ m]
        else: 
            numbers=  calc(m, n-1, inp-m) +[m]  #move to side
    return numbers 

def path(num_list):
    path= ""
    num_list.sort(reverse= True)
    for x in range(1, len(num_list)):
        if num_list[x] == num_list[x-1]:
            path = path+ "R"
        else: 
            path= path + "D"
    return path

def operation(m, n, summed_num):
    return summed_num, path(calc(m,n, summed_num))
        
sum1, path1= operation(9,9,65)
sum2, path2=operation(9,9,72)
sum3, path3=operation(9,9,90)
sum4, path4=operation(9,9,110)


print("//---------------Output---------------//")
print("1a")
print("{sum} {path}".format(sum= sum1, path= path1))
print("{sum} {path}".format(sum= sum2, path= path2))
print("{sum} {path}".format(sum= sum3, path= path3))
print("{sum} {path}".format(sum= sum4, path= path4))

print("1b")
m=90000
n=100000
sum5, path5 = operation(m, n, 87127231192)
print("{sum} {path}".format(sum= sum5, path= path5))

