#!/usr/bin/env python
# coding: utf-8

# In[26]:


import re
import json


# In[27]:


file_data = []


# In[28]:


with open('topics-rnd5.xml') as topic_reader:
    file_data = topic_reader.read()


# In[29]:


topics = re.findall("<query>([\s\S\n]*?)</query>", file_data )


# In[30]:


train_queries = []
test_queries = []
for i in range(1, 50, 2):
    train_queries.append(topics[i-1])
    test_queries.append(topics[i])


# In[31]:


topic_dict = ({'train': train_queries, 'test' : test_queries})
with open('topics.json', 'w') as outfile:
    json.dump(topic_dict, outfile)

