#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import json


# In[2]:


with open("qrels-covid_d5_j0.5-5.txt", "r") as file:
    Lines = file.readlines() 


# In[3]:


len(Lines)


# In[4]:


for i in range(len(Lines)): 
    line = Lines[i].strip()
    line = line.split(" ")
    Lines[i] = line


# In[5]:


query = []
row_data = []
for row in Lines:
    row_data = []
    row_data.append([row[0], row[2], row[3]] )
    query.append(row_data[0])


# In[6]:


query_dict = ({ 'query': query })
with open('query.json', 'w') as outfile:
    json.dump(query_dict, outfile)

