#!/usr/bin/env python
# coding: utf-8

# In[70]:


import pandas as pd
import datetime


# In[71]:


import numpy as np


# Importing data...

# In[116]:


df=pd.read_csv("ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt", header = None, skiprows = 72,
               delim_whitespace = True, usecols = [0,1,3,4,5,6], names = ['Year', 'Month', 'Real Average', 'Interpolated Average', 'Season Trend', 'Date'], na_values =  -1)


# In[117]:


df.head()


# Extracting 3 columns with index provided

# In[18]:


df1=df.iloc[:,[0,1,3]] #choosing columns to show
print(df1.head())


# In[39]:


for index, row in df.iterrows(): #Need to use "index, row" with iterrows()
    if row['Real Average'] == -99.99: row['Real Average'] = np.nan #np.nan substitutes null value
    #print(row['Real Average'])
    


# In[81]:


df.columns = ['Year', 'Month', 'CO2', 'Interpolated Average', 'Season Trend', 'Date'] #couldn't change just one header by indexing it, had to rename all of them
print(df.columns)


# In[82]:


df['Day']= 15 # or [15]*len(df) #you can broadcast the value (autofill) if you don't put the value in a list
df.head()


# In[87]:


date_list=[]
for index, row in df.iterrows():
    date_list.append(datetime.date(int(row['Year']), int(row['Month']), int(row['Day'])))
#needs to be INT type...inside dataframe is detfaults INT64, which was interpreted as a float. used df.dtypes to see what the various data types are in the dataframe
df['Second Date']=date_list
df.head()


# In[89]:


df.dtypes


# In[103]:


df.drop(labels= 'Day', axis = 1, inplace=True) #we have to specify INPLACE =TRUE so it replaces the original dataframe with new information, instead of just doing it once. 


df.head()


# In[106]:



df.iloc[:,[0,2]].groupby('Year').mean().head() #Used iLoc to isolate specific columns and rows, then used GROUPBY function on that specific set. Then specified what to do with that information (mean)


# In[118]:


npdata=df.iloc[:,[2,6]].as_matrix() #converting to numpy array

#print(npdata)


# In[119]:


df.head()


# In[126]:


x = df.iloc[:,2]
df['Real Average']= np.where( x== -99.99, np.nan, x)
df.head()


# In[ ]:




