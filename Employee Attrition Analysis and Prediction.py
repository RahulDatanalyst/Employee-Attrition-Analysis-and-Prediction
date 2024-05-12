#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
style.use('fivethirtyeight')
sns.set(style='whitegrid',color_codes=True)


# In[3]:


import warnings
warnings.filterwarnings("ignore")


# In[4]:


df=pd.read_csv(r"C:\Users\hp\Downloads\Employee_Attrition.csv")
df.head()


# In[5]:


df.columns


# In[49]:


df.info()


# In[25]:


df.shape


# In[50]:


df.describe()


# In[24]:


df.isnull().sum()


# In[15]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')


# In[19]:


df.head()


# In[6]:


df.columns


# In[23]:


df.describe()


# In[ ]:


#univariate analysis


# In[26]:


df.describe()


# In[9]:


sns.catplot(data=df,kind='box',height=10,aspect=3)


# In[6]:


sns.kdeplot(df['Age'],fill=True,color='#ff4125')


# In[9]:


sns.histplot(df['Age'])


# In[10]:


fig,ax = plt.subplots(5,2, figsize=(9,9))
sns.histplot(df['TotalWorkingYears'], ax = ax[0,0])
sns.histplot(df['MonthlyIncome'], ax = ax[0,1])
sns.histplot(df['YearsAtCompany'], ax = ax[1,0])
sns.histplot(df['DistanceFromHome'], ax = ax[1,1])
sns.histplot(df['YearsInCurrentRole'], ax = ax[2,0])
sns.histplot(df['YearsWithCurrManager'], ax = ax[2,1])
sns.histplot(df['YearsSinceLastPromotion'], ax = ax[3,0])
sns.histplot(df['PercentSalaryHike'], ax = ax[3,1])
sns.histplot(df['YearsSinceLastPromotion'], ax = ax[4,0])
sns.histplot(df['TrainingTimesLastYear'], ax = ax[4,1])
plt.tight_layout()
plt.show()


# In[11]:


cat_df=df.select_dtypes(include='object')


# In[54]:


cat_df.columns


# In[10]:


def plot_cat(attr, labels=None):
    if attr == 'JobRole':
        sns.catplot(data=df, kind='count', height=5, aspect=3, x=attr)
        return

    sns.catplot(data=df, kind='count', height=5, aspect=1.5, x=attr)


# In[11]:


plot_cat('Attrition')


# In[12]:


plot_cat('BusinessTravel')


# In[14]:


plot_cat('OverTime')


# In[15]:


plot_cat('Department')


# In[16]:


plot_cat('EducationField')


# In[17]:


plot_cat('Gender')


# In[18]:


plot_cat('JobRole')


# In[19]:


plot_cat('Education')


# In[21]:


plot_cat('JobSatisfaction')


# In[31]:


num_disc = ['Education', 'EnvironmentSatisfaction', 'JobInvolvement', 'JobSatisfaction', 'WorkLifeBalance', 'RelationshipSatisfaction', 'PerformanceRating']

def plot_cat(attr, labels=None):
    if attr == 'JobRole':
        sns.catplot(data=df, kind='count', height=5, aspect=3, x=attr)
        plt.show()  # Display the plot
        return

    sns.catplot(data=df, kind='count', height=5, aspect=1.5, x=attr)
    plt.show()  # Display the plot

for i in num_disc:
    plot_cat(i)


# In[35]:


cor_mat= df.corr()
mask = np.array(cor_mat)
mask[np.tril_indices_from(mask)] = False
fig=plt.gcf()
fig.set_size_inches(30,12)
sns.heatmap(data=cor_mat,mask=mask,square=True,annot=True,cbar=True)


# In[37]:


sns.catplot(data=df,y='Age',x='Attrition',height=5,aspect=1,kind='box')


# In[38]:


df.Department.value_counts()


# In[39]:


sns.catplot(data=df,kind='count',x='Attrition',col='Department')


# In[40]:


pd.crosstab(columns=[df.Attrition],index=[df.Department],margins=True,normalize='index')


# In[41]:


pd.crosstab(columns=[df.Attrition],index=[df.Gender],margins=True,normalize='index')


# In[42]:


pd.crosstab(columns=[df.Attrition],index=[df.JobLevel],margins=True,normalize='index')


# In[44]:


sns.catplot(data=df,kind='bar',x='Attrition',y='MonthlyIncome')


# In[46]:


sns.catplot(data=df,kind='count',x='Attrition',col='JobSatisfaction')


# In[47]:


pd.crosstab(columns=[df.Attrition],index=[df.JobSatisfaction],margins=True,normalize='index')


# In[48]:


pd.crosstab(columns=[df.Attrition],index=[df.EnvironmentSatisfaction],margins=True,normalize='index')


# In[49]:


pd.crosstab(columns=[df.Attrition],index=[df.JobInvolvement],margins=True,normalize='index')


# In[50]:


pd.crosstab(columns=[df.Attrition],index=[df.WorkLifeBalance],margins=True,normalize='index')


# In[52]:


pd.crosstab(columns=[df.Attrition],index=[df.RelationshipSatisfaction],margins=True,normalize='index')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




