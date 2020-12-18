#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[19]:


import csv
Lines = [] 
column_names = []
with open('metadata.csv', encoding="latin-1") as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in reader:
        if line_count == 0:
            column_names = row
            line_count += 1
        else:
            Lines.append([row[0] , row[3], row[8]])


# In[20]:


id_header = "cord_uid"
title_header = "title"
abstract_header = "abstract"


# In[21]:


# Output id, title and abstract into data.csv ==> metadata.csv ~= 250 mb data.csv ~= 200 mb
with open('data.csv', 'w', newline='', encoding="latin-1") as file:
    fieldnames = [id_header, title_header, abstract_header]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in Lines:
        writer.writerow({ fieldnames[0] : row[0], fieldnames[1]: row[1], fieldnames[2]: row[2] })


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




