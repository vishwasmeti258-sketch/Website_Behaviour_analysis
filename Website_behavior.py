import numpy as np
import pandas as pd
import matplotlib.pyplot as  plt
import seaborn as sb

#-----------------------------------------------------------------------------------------------------------
#data importing
#-------------------------------------------------------------------------------------------------
df =pd.read_csv('csv/website_wata.csv')
print(df.head())
print(df.describe())

#-----------------------------------------------------------------------------------------------------------
#data cleaning
#-------------------------------------------------------------------------------------------------
print(df.isnull().sum())
print(df.nunique())

#-----------------------------------------------------------------------------------------------------------
# Data manipulation
#-------------------------------------------------------------------------------------------------
df['Session Duration'] = df['Session Duration'].round(2)
df['Bounce Rate'] = df['Bounce Rate'].round(2)*100
df['Time on Page'] = df['Time on Page'].round(1)

#-----------------------------------------------------------------------------------------------------------
# Data_visualization
#-------------------------------------------------------------------------------------------------

#count of different people came different soucre
sf = df['Traffic Source'].value_counts().plot(kind='line',marker='o')
plt.title('Traffic source count')
plt.show()

sb.pairplot(df,vars=['Time on Page','Bounce Rate','Previous Visits','Conversion Rate','Page Views'],
hue='Traffic Source')
plt.show()

Cmatrix = df[['Page Views','Session Duration','Bounce Rate','Time on Page','Previous Visits','Conversion Rate']].corr()
sb.heatmap(Cmatrix,annot=True,cmap='coolwarm')
plt.show()

plt.barh('Page Views','Session Duration',data=df)
plt.title('Views vs Duration')
plt.xlabel('pages views')
plt.ylabel('Duration')
plt.show()

plt.bar('Previous Visits','Conversion Rate',data=df)
plt.title('perv. visits vs rate of converation')
plt.xlabel('Visits')
plt.ylabel('Conversion')
plt.show()

# violion plot
sb.violinplot(x='Traffic Source',y='Time on Page',data=df)
plt.title('Density of time on page by sources')
plt.show()

sb.violinplot(x='Traffic Source',y='Bounce Rate',data=df)
plt.title('Density of Bounce Rate by sources')
plt.show()

sb.boxplot(x='Traffic Source',y='Session Duration',data=df)
plt.title('to see any outlier')
plt.show()

#-------------------------------------------------------------------------------------------------------------------------
#data_exporting
#-------------------------------------------------------------------------------------------------------------------------
df.to_csv('Cleaned_web_dataset.csv',index=False)