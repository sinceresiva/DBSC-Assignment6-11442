import numpy as np
import pandas as pd

url=".//US_Baby_Names_right.csv"
df = pd.read_csv(url)

#Print the data frame
print(df)

#Delete unnamed column
df=df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1)
print(df)

#Show the distribution of male and female
df_dist_sex=df.groupby(by=['Gender'])['Count'].sum()
print(df_dist_sex)
df.groupby(by=['Gender'])['Count'].hist()

#Show the top 5 most preferred names
df_names=df.groupby(by=['Name'])['Count']
df_names=df_names.sum().reset_index(name ='Name_Count')
df_popular_names=df_names.sort_values('Name_Count',ascending=False)
print(df_popular_names.head(5))

#What is the median name occurence in the dataset
md=np.median(df["Id"])
df.loc[df['Id'] == md]["Name"]

#Distribution of male and female born count by states
df_dist_sex=df.groupby(by=['State','Gender'])['Count'].sum()
print(df_dist_sex)