# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:21:16 2018

@author: Yijie
"""

#Q4:
#(1)
yours = ['Yale','MIT','Berkeley']
mine = ['Harvard','CAU','Stanford']
ours1 = mine + yours
ours2=[]
ours2.append(mine)
ours2.append(yours)
print(ours1)
print(ours2)
# Difference:the print out results indicate that the list 'ours1' is having 
#the objects in 'yours' and 'mine' together, while 'ours2' has a dividing line
# between 'yours' and 'mine'.

#(2) question: do you want to remove something?
yours[1]='Mich'
print(ours1)
print(ours2)
#ours1 stays unchanged while ours2 changed because ours1 is a new list, while ours2 is adding 