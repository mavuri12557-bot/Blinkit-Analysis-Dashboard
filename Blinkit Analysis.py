#!/usr/bin/env python
# coding: utf-8

# ## Data Analysis Python Project - Blinkit Analaysis

# ### Import libraries

# In[29]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# #### Import Raw Data
# 

# In[2]:


df = pd.read_csv("C:/Users/mavur/Downloads/Grocery_data/BlinkITGroceryData.csv")


# #### Sample Data
# 
# 

# In[3]:


df.head(20)


# In[4]:


df.tail(9)


# #### Size of Data
# 

# In[5]:


print("Size of data",df.shape)


# ### Feild Info

# In[6]:


df.columns


# ### Data Types
# 

# In[7]:


df.dtypes


# ### Data Cleaning

# In[8]:


print(df['Item Fat Content']. unique())


# In[9]:


df['Item Fat Content'] = df['Item Fat Content'].replace({'LF': 'Low Fat', 'low fat':'Low Fat','reg':'Regular'})


# In[10]:


print(df['Item Fat Content']. unique())


# In[11]:


print(df['Item Fat Content']. unique())


# In[12]:


df['Item Fat Content'] = df['Item Fat Content'].replace({'LF': 'Low Fat', 'low fat':'Low Fat','reg':'Regular'})


# In[13]:


print(df['Item Fat Content']. unique())


# In[14]:


df['Item Fat Content'] = df['Item Fat Content'].replace({'low fat':'Low Fat'})


# In[15]:


print(df['Item Fat Content']. unique())


# In[16]:


df['Item Fat Content'] = df['Item Fat Content'].replace({'Low fat':'Low Fat'})


# In[17]:


print(df['Item Fat Content'].unique())


# ## Business Requiremnets

# ### Kpi's Requirements

# In[28]:


# Total Sales
total_sales = df['Sales'].sum()

# Average Sales
average_sales = df['Sales'].mean()

# Number of Items Sold
no_of_items_sold = df['Sales'].count()

# Average Rating
average_rating = df['Rating'].mean()

# Display all metrics
print(f"Total Sales: ${total_sales:,.0f}")
print(f"Average Sales: ${average_sales:,.0f}")
print(f"Number of Items Sold: {no_of_items_sold:,}")
print(f"Average Rating: {average_rating:.0f}")


# ### Chart's Requirements

# ### Total sales by Fat Content

# In[32]:


# Total sales by Fat Content

sales_by_fat = df.groupby('Item Fat Content')['Sales'].sum()

plt.pie(sales_by_fat, labels=sales_by_fat.index,
        autopct='%1.1f%%', 
        startangle=90)
plt.title('Sales by Fat Content')
plt.axis('equal')
plt.show()


# ### Total sales by Item Type
# 

# In[35]:


sales_by_type = df.groupby('Item Type')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
bars = plt.bar(sales_by_type.index, sales_by_type.values)

plt.xticks(rotation=90)
plt.xlabel('Item Type')
plt.ylabel('Total Sales')
plt.title('Total Sales by Item Type')

for bar in bars:
    plt.text(bar.get_x()+ bar.get_width()/2, bar.get_height(),
            f'{bar.get_height():,.0f}', ha='center', va='bottom',fontsize=8)
    
plt.tight_layout()
plt.show()


# ### Fat Content by Outlet for Total Sales
# 

# In[36]:


grouped = df.groupby(['Outlet Location Type', 'Item Fat Content'])['Sales'].sum().unstack()
grouped = grouped[['Regular', 'Low Fat']]

ax = grouped.plot(kind='bar', figsize=(8,5), title='Outlet Tier by Item Fat Contet')
plt.xlabel('Out Location Tier')
plt.ylabel('Total Sales')
plt.legend(title='Item Fat Content')
plt.tight_layout()
plt.show()


# ### Total Sales by Outlet Establishment

# In[37]:


sales_by_year = df.groupby('Outlet Establishment Year')['Sales'].sum().sort_index()

plt.figure(figsize=(9,5))
plt.plot(sales_by_year.index, sales_by_year.values, marker='o', linestyle='-')

plt.xlabel('Outlet Establishment Year')
plt.ylabel('Total Sales')
plt.title('Outlet Establishment')

for x,y in zip(sales_by_year.index, sales_by_year.values):
    plt.text(x,y,f'{y:,.0f}', ha='center', va='bottom', fontsize=8)
    
plt.tight_layout()
plt.show()


# ### Sales by Outlet Size

# In[38]:


sales_by_size = df.groupby('Outlet Size')['Sales'].sum()

plt.figure(figsize=(4,4))
plt.pie(sales_by_size, labels=sales_by_size.index, autopct='%1.1f%%', startangle=90)
plt.title('Outlet Size')
plt.tight_layout()
plt.show()


# ### Sales by Outlet LOcation

# In[40]:


sales_by_location = df.groupby('Outlet Location Type')['Sales'].sum().reset_index()
sales_by_location = sales_by_location.sort_values('Sales', ascending=False)

plt.figure(figsize=(8,3))  ##Smaller height, enough width
ax= sns.barplot(x='Sales', y='Outlet Location Type', data=sales_by_location)


plt.title = ('Total Sales by Outlet Location Type')
plt.xlabel = ('Total Sales')
plt.ylabel = ('Outlet Location Type')

plt.tight_layout()
plt.show()


# In[ ]:




