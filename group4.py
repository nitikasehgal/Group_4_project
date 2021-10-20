#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data=pd.read_csv("C:\\Users\\NITIKA\\OneDrive\\Desktop\\Demo\\dataset1.csv")
data.head()


# In[58]:


X=data.groupby(['Year']).count()


# In[59]:


X


# In[3]:


data.groupby(["Year","winning team"]).max().reset_index().drop(columns="Unnamed: 2").to_csv("C:\\Users\\NITIKA\\OneDrive\\Desktop\\Demo\\New_file.csv")


# In[4]:


x=data.groupby(["Year","winning team"]).count().reset_index()
x


# In[5]:


n_1930=x[x["Year"]==1930]


# In[105]:


n_1930=n_1930.sort_values("Stage",ascending=False).head(2)
n_1930


# In[7]:


n_1930


# In[8]:


pd.set_option("max_rows",None)
pd.set_option("max_columns",None)


# In[9]:


x["Year"].value_counts().count()


# In[10]:


n_1934=x[x["Year"]==1934]


# In[11]:


n_1934=n_1934.sort_values("Stage",ascending=False).head(1)
n_1934


# In[12]:


n_1938=x[x["Year"]==1938]


# In[13]:


n_1938=n_1938.sort_values("Stage",ascending=False).head(1)
n_1938


# In[24]:


n_1950=x[x["Year"]==1950]


# n_1950=n_1950.sort_values("Stage",ascending=False).head(2)
# n_1950

# In[26]:


n_1950=n_1950.sort_values("Stage",ascending=False).head(2)


# In[27]:


n_1950


# In[28]:


n_1954=x[x["Year"]==1954]


# In[30]:


n_1954=n_1954.sort_values("Stage",ascending=False).head(1)
n_1954


# In[31]:


n_1958=x[x["Year"]==1958]


# In[33]:


n_1958=n_1958.sort_values("Stage",ascending=False).head(1)
n_1958


# In[34]:


n_1962=x[x["Year"]==1962]


# In[36]:


n_1962=n_1962.sort_values("Stage",ascending=False).head(1)
n_1962


# In[40]:


n_1966=x[x["Year"]==1966]


# In[42]:


n_1966=n_1966.sort_values("Stage",ascending=False).head(2)
n_1966


# In[43]:


n_1970=x[x["Year"]==1970]


# In[45]:


n_1970=n_1970.sort_values("Stage",ascending=False).head(1)
n_1970


# In[49]:


n_1974=x[x["Year"]==1974]


# In[51]:


n_1974=n_1974.sort_values("Stage",ascending=False).head(2)
n_1974


# In[60]:


n_1978=x[x["Year"]==1978]


# In[62]:


n_1978=n_1978.sort_values("Stage",ascending=False).head(1)
n_1978


# In[63]:


n_1982=x[x["Year"]==1982]


# In[65]:


n_1982=n_1982.sort_values("Stage",ascending=False).head(1)
n_1982


# In[66]:


n_1986=x[x["Year"]==1986]


# In[68]:


n_1986=n_1986.sort_values("Stage",ascending=False).head(1)
n_1986


# In[69]:


n_1990=x[x["Year"]==1990]


# In[71]:


n_1990=n_1990.sort_values("Stage",ascending=False).head(1)
n_1990


# In[72]:


n_1994=x[x["Year"]==1994]


# In[74]:


n_1994=n_1994.sort_values("Stage",ascending=False).head(1)
n_1994


# In[75]:


n_1998=x[x["Year"]==1998]


# In[77]:


n_1998=n_1998.sort_values("Stage",ascending=False).head(1)
n_1998


# In[81]:


n_2002=x[x["Year"]==2002]


# In[83]:


n_2002=n_2002.sort_values("Stage",ascending=False).head(1)
n_2002


# In[94]:


n_2006=x[x["Year"]==2006]


# In[95]:


n_2006=n_2006.sort_values("Stage",ascending=False).head(5)
n_2006


# In[98]:


n_2010=x[x["Year"]==2010]


# In[99]:


n_2010=n_2010.sort_values("Stage",ascending=False).head(2)
n_2010


# In[100]:


n_2014=x[x["Year"]==2014]


# In[102]:


n_2014=n_2014.sort_values("Stage",ascending=False).head(1)
n_2014


# In[106]:


fifa=pd.concat([n_1930, n_1934, n_1938, n_1950, n_1954, n_1958, n_1962, n_1966, n_1970, n_1974, n_1978, n_1982, n_1986, n_1990, n_1994, n_1998, n_2002, n_2006, n_2010, n_2014])


# In[131]:


fifa_new=fifa.groupby("winning team").count().reset_index()
fifa_new


# In[123]:


fifa


# In[114]:


data1=pd.read_csv("C:/Users/NITIKA/Downloads/world_cup_2018.csv")
data1.head()


# In[127]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[140]:


fig=plt.figure(figsize=(18,15))
sns.barplot(fifa_new["winning team"],fifa_new["Stage"])
plt.show()
fig.savefig("C:/Users/NITIKA/Downloads/plot/fig.pdf")

