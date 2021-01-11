#!/usr/bin/env python
# coding: utf-8

# In[13]:


###write a program which will find all such numbers which are divisble by 7 but are not a multiple of 5,between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line
number=[]
for x in range(2000,3200):
    if x%7==0 and x%5!=0:
        number.append(str(x))
print(','.join(number))


# In[2]:


##write a python program to accept the users first and last name and then getting them printed in the reverse order with a space between first name and last name
first_name=input("enter the first name:" )
last_name=input("enter the last name:" )
print(last_name, first_name)


# In[7]:


##write a python program to find the volume of a sphere with diameter 12cm
d=12
r=d/2
volume=4/3*3.142*r*r*r
print(volume)


# In[ ]:




