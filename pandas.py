#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd


# ### Loading the file

# In[27]:


df = pd.read_csv(r"C:\Users\17819\OneDrive\Desktop\pandas\COVID-19 Coronavirus.csv")


# ### Cleaning the Dataset

# In[28]:


df.head(10)


# In[29]:


df.tail(10)


# In[30]:


df.describe()


# In[31]:


df.info()


# In[34]:


missing_data = df.isnull().sum()


# In[35]:


print(missing_data)


# ###  Handling the missing values

# In[38]:


df['Other names'].fillna(df['Other names'].mode()[0], inplace=True)


# In[39]:


df


# In[40]:


df.drop_duplicates()


# In[42]:


print(df.dtypes)


# In[43]:


df['CFR (%)'] = (df['Total Deaths'] / df['Total Cases']) * 100


# In[44]:


df


# In[45]:


top_cases = df.sort_values(by='Total Cases', ascending=False).head(10)
print(top_cases[['Country', 'Total Cases']])


# In[46]:


top_death_percent = df.sort_values(by='Death percentage', ascending=False).head(10)
print(top_death_percent[['Country', 'Death percentage']])

