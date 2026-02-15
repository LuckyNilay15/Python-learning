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
#print(df.isnull().sum(axis=1)) #axis=1 means row wise
#print(df.isnull().sum(axis=0)) #axis=0 means column wise

description=df.describe(include="all")
# print(description)

#unique values from gender column

uniquegender=df['Gender'].unique()
# print(uniquegender)

#count of each unique value
eachuniquevalue=df['Gender'].value_counts()
# print(eachuniquevalue)

Marks=df[(df['Marks']>=90) & (df['Marks']<=100)]
# print(Marks)

#unsing between method

Marks=df[df['Marks'].between(90,100)]
# print(Marks)

#Average of marks
average=df['Marks'].mean()
print(average)

def marks(x):
    return x/2 # use // for integer division

df['Half_Marks']=df['Marks'].apply(marks)
print(df)

df['Half_Marks_lambda']=df['Marks'].apply(lambda x:x/2)
print(df)
