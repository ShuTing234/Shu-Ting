# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 10:20:18 2020

@author: TANST
"""

#---------------------Question 1---------------------
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
        if sum(calc(m-1, n, inp-m) +[ m]) == inp: #move up
            numbers= calc(m-1, n, inp-m) +[ m]
        else: 
            numbers=  calc(m, n-1, inp-m) +[m]  #move to side
    return numbers 

def route(num_list):
    path= ""
    num_list.sort(reverse= True)
    for x in range(1, len(num_list)):
        if num_list[x] == num_list[x-1]:
            path = path+ "R"
        else: 
            path= path + "D"
    return path

def operation(m, n, summed_num):
    return summed_num, route(calc(m,n, summed_num))
    
#//---------------Output---------------//
# 1a

output1= open("Question 1\output_question_1", "w")
m, n= 9,9
input_q1= [65,72, 90, 110]
output=[]
for num in input_q1:
    summed_num, path= operation(m,n, num)
    output.append([summed_num, path])
    output1.write("{summed_num} {path}\n".format(summed_num= summed_num, path= path))
output1.close()


print("1b")
m=90000
n=100000
sum5, path5 = operation(m, n, 87127231192)
output1= open("Question 1\output_question_1", "w+")
output1.write("{summed_num} {path}\n".format(summed_num= sum5, path= path5))


output1.close()


#---------------------Question 6---------------------"

from shapely.geometry import Polygon, Point
# read polygon coordinates
poly=[]
f = open("Question 6\input_question_6_polygon", "r")
for line in f.readlines():
    coor= line.strip()
    x, y= coor.split(" ")
    poly.append([float(x),float(y)])
f.close()
poly1= Polygon(tuple(poly))

# read the list of points 
points= []
f2= open("Question 6\input_question_6_points", "r")
for line in f2.readlines():
    pt= line.strip()
    x, y = pt.split(" ")
    points.append(Point(float(x),float(y)))
f2.close()

output6= open("Question 6\output_question_6", "w")
for pt in points:
    if pt.within(poly1) == True:
        ans= "Inside"
    else:
        ans= "Outside"
    
    output6.write("{x} {y} {ans}\n".format(x= pt.x, y=pt.y, ans= ans))
    
    # output6.write("/n")
output6.close()


#---------------------Question 8---------------------"
# d[ES]/ dt = k1[E][S]
# d[P] / dt = k3[ES]
# d[S] / dt = k2[ES] - k1[E][S]
# d[E] / dt = (k2 + k3)[ES] - k1[E][S] 
