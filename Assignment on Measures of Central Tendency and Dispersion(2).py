#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
import seaborn as sns


# In[7]:


df = pd.read_csv("StudentsPerformance (1).csv")
df


# In[8]:


### 1 .Find out how many males and females participated in the test


# In[9]:


print(list(df['gender']).count('female'))
print(list(df['gender']).count('male'))


# In[13]:


### What do you think about the students' parental level of education?


# In[19]:


df['parental level of education'].value_counts()


# In[56]:


### Who scores the most on average for math, reading and writing based on
   ## Gender


# In[22]:


test = df[['gender', 'math score', 'reading score', 'writing score']]
test.head(10)


# In[23]:


female = test['gender'] == 'female'
test[female].head()


# In[24]:


male = test['gender'] == 'male'
test[male].head()


# In[29]:


fe_avg = test[female]['math score'].mean()
male_avg = test[male]['math score'].mean()
df_math = pd.DataFrame({'Gender': ['female', 'male'], 'average math score': [fe_avg, male_avg]})
df_math


# In[28]:


fe_avg = test[female]['reading score'].mean()
male_avg = test[male]['reading score'].mean()
df_math = pd.DataFrame({'Gender': ['female', 'male'], 'average reading score': [fe_avg, male_avg]})
df_math


# In[57]:


fe_avg = test[female]['writing score'].mean()
male_avg = test[male]['writing score'].mean()
df_math = pd.DataFrame({'Gender': ['female', 'male'], 'writing score': [fe_avg, male_avg]})
df_math


# In[ ]:


### Who scores the most on average for math, reading and writing based on
   ## Test Prepration


# In[39]:


df1=df.loc[df['test preparation course'] == 'none', 'math score'].mean()
df2=df.loc[df['test preparation course'] == 'completed', 'math score'].mean()
df_math = pd.DataFrame({'test preparation course': ['none', 'completed'], 'math score': [df1, df2]})
df_math


# In[41]:


df3=df.loc[df['test preparation course'] == 'none', 'reading score'].mean()
df4=df.loc[df['test preparation course'] == 'completed', 'reading score'].mean()
df_math = pd.DataFrame({'test preparation course': ['none', 'completed'], 'reading score': [df3, df4]})
df_math


# In[42]:


df5=df.loc[df['test preparation course'] == 'none', 'writing score'].mean()
df6=df.loc[df['test preparation course'] == 'completed', 'writing score'].mean()
df_math = pd.DataFrame({'test preparation course': ['none', 'completed'], 'writing score': [df5, df6]})
df_math


# In[61]:


###  What do you think about the scoring variation for math, reading and writing based on
### Gender


# In[43]:


test1 = df[['gender', 'math score', 'reading score', 'writing score']]
test1.head()


# In[45]:


df.var()


# In[47]:


fe_var = test1[female]['math score'].var()
male_var = test1[male]['math score'].var()
df_math = pd.DataFrame({'Gender': ['female', 'male'], 'math score': [fe_var, male_var]})
df_math


# In[48]:


fe_var = test1[female]['reading score'].var()
male_var = test1[male]['reading score'].var()
df_math = pd.DataFrame({'Gender': ['female', 'male'], 'reading score': [fe_var, male_var]})
df_math


# In[58]:


fe_var = test1[female]['writing score'].var()
male_var = test1[male]['writing score'].var()
df_math = pd.DataFrame({'Gender': ['female', 'male'], 'writing score': [fe_var, male_var]})
df_math


# In[ ]:


### Who scores the most on average for math, reading and writing based on
   ## Test Prepration


# In[50]:


df7=df.loc[df['test preparation course'] == 'none', 'math score'].var()
df8=df.loc[df['test preparation course'] == 'completed', 'math score'].var()
df_math = pd.DataFrame({'test preparation course': ['none', 'completed'], 'math score': [df7, df8]})
df_math


# In[52]:


df9=df.loc[df['test preparation course'] == 'none', 'reading score'].var()
df10=df.loc[df['test preparation course'] == 'completed', 'reading score'].var()
df_math = pd.DataFrame({'test preparation course': ['none', 'completed'], 'reading score': [df9, df10]})
df_math


# In[53]:


df11=df.loc[df['test preparation course'] == 'none', 'writing score'].var()
df12=df.loc[df['test preparation course'] == 'completed', 'writing score'].var()
df_math = pd.DataFrame({'test preparation course': ['none', 'completed'], 'writing score': [df11, df12]})
df_math


# In[64]:


df.nlargest(250, ['math score'])


# In[63]:


df['math score'].nlargest(250)

