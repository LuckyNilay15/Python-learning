import numpy as np
data=np.array([1,2,3,4,5])
print(data+10) #vectorization

arr1=np.array([1,2,3])
print(arr1.ndim)

months=np.array(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
sales=[]
print("Enter the sales for each month ")

for month in months:
    value=float(input(f"{month}"))
    sales.append(value)

sales=np.array(sales)
print("\n Company sales analysis--------")

print("Total sales of the year", np.sum(sales))
print("Average slaes per momth",np.mean(sales))
print("Max sale in the year", np.max(sales))
print("Min sales of the year", min(sales))



