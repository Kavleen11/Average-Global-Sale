#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pymysql


# In[2]:


import pandas as pd
from sqlalchemy import create_engine
import pymysql


# In[3]:


# create engine
engine = create_engine('mysql+pymysql://root:Kavleen.24@localhost/data1202')


# In[4]:


# connection string
conn = engine.connect()


# In[5]:


# read a simple query into DataFrame
df = pd.read_sql("SELECT * FROM data1202.vgsales_2016", conn)


# In[6]:


# print DataFrame
print(df.head())


# In[7]:


# Calculate average global sales before and after 2005
avg_sales_before_2005 = df[df['Year_of_Release'] <= 2005]['Global_Sales'].mean()
avg_sales_after_2005 = df[df['Year_of_Release'] > 2005]['Global_Sales'].mean()


# In[8]:


# Print results
print("Average global sales before 2005:", avg_sales_before_2005)
print("Average global sales after 2005:", avg_sales_after_2005)


# In[9]:


#add a new column
df['Era'] = df['Year_of_Release'].apply(lambda year: 'pre-2005' if year <= 2005 else 'post-2005')


# In[10]:


print(df.head())


# In[ ]:




