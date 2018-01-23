# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:01:02 2018

@author: Yijie
"""
#Q1
x=17
y1=int(x)
y2=float(x)
y3=str(x)
y4=bool(x>18)
print(y1,y2,y3,y4)
print(type(y1),type(y2),type(y3),type(y4))

# '+' could serve to connect characters.
text=('The '+'value '+'of '+'x '+'is '+str(y1))
print(text)