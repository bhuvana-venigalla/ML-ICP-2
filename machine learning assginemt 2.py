#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question1
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")


# In[2]:


#Question2 
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for index, value in enumerate(my_list):
    if index % 2 != 0:
        print(value)


# In[3]:


#Question3
n = [23, 'Python',23.98]
x = []
for i in range(len(n)):
    x.append(type(n[i]))
print(n)
print(x)


# In[4]:


#Question4
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 


# In[5]:


#Question5
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brow Fox')


# In[ ]:




