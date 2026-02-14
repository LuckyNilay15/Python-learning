import pandas as pd

dict1={     #python dictionary
    "Name":["John", "Anna", "James", "Linda"],
    "Marks":[85,92,88,95],
    "Gender":["M","F","M","F"]
}

df=pd.DataFrame(dict1)
#print(df)

#top 3 rows
top3=df.head(3)
#print(top3)

#last 3 rows
last3=df.tail(3)
#print(last3)

#shape of dataset

shape=df.shape #shape is not a method its an attribute of pandas data frame
#print(shape)

#print(df.info()) # In Pandas, object is the standard data type for columns containing text or mixed values.

#check null values
print(df.isnull().sum(axis=1)) #axis=1 means row wise
print(df.isnull().sum(axis=0)) #axis=0 means column wise





