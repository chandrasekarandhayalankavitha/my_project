
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(".github/week8/FoodDelivery_Dataset.csv.xls")

#q1
mintime = df["Delivery Time"].min()
maxtime = df["Delivery Time"].max()
avgtime = df["Delivery Time"].mean()
print("min:", mintime, "max:", maxtime, "avg:", avgtime)

#q2
count = (df["Order Amount"]>1000).sum()
print("ordersabv1000:", count)

#q3
rating5 = (df["Rating"]==5).sum()
rating3 = (df["Rating"]==3).sum()
rating1 = (df["Rating"]==1).sum()
print("rating1:", rating1, "rating3", rating3, "rating5", rating5)

#q4
subset = df.iloc[[0, 9, 19, 39, 59]]
plt.scatter(subset["Distance"], subset["Delivery Time"])
plt.xlabel("Distance")
plt.ylabel("Delivery Time")
plt.show()

#q5
plt.scatter(subset["Distance"], subset["Rating"])
plt.xlabel("Distance")
plt.ylabel("Rating")
plt.show()

#q6
discount1km = df[df["Distance"]==1]
discount79 = df[df["Distance"].between(7,9)]
plt.boxplot([discount1km["Discount"], discount79["Discount"]],labels=['1km','7km'])
plt.ylabel("Discount")
plt.show()

#q7
rating5 = df[df["Rating"] == 5].head(3)
print(rating5)

#q8
rating1 = df[df["Rating"]==1].head(3)
print(rating1)

#q9
#a) Distance <-> Delivery Time -- positive  
#b) Distance <-> Customer Rating -- negative    
#c) Items Ordered <-> Order Amount 
plt.scatter(df["Items Ordered"], df["Order Amount"])
plt.xlabel("Items Ordered")
plt.ylabel("Ordered Amount")
plt.show() 
#d) Discount % <-> Customer Rating 
plt.scatter(df["Discount"], df["Rating"])
plt.xlabel("Discount")
plt.ylabel("Rating")
plt.show() 

#q10
rating1 = df[df["Rating"]==1].head(5)
print(rating1)
rating2 = df[df["Rating"] == 2].head(5)
print(rating2)
rating3 = df[df["Rating"] == 3].head(5)
print(rating3)
rating4 = df[df["Rating"] == 4].head(5)
print(rating4)
rating5 = df[df["Rating"] == 5].head(5)
print(rating5)

#partb
#q11,12,13,14
q1 = np.percentile(df["Delivery Time"],25)
print(q1)
q3 = np.percentile(df["Delivery Time"],75)
print(q3)
iqr = q3-q1
print(iqr)
lowerbound = q1 - 1.5*iqr
print(lowerbound)
upperbound = q3 + 1.5*iqr
print(upperbound)
outliers=[]
for i in range(len(df)):
    if df["Delivery Time"][i] < lowerbound or df["Delivery Time"][i] > upperbound:
        outliers.append(df["Order"][i])
print(outliers)

#q15
q1 = np.percentile(df["Order Amount"],25)
print(q1)
q3 = np.percentile(df["Order Amount"],75)
print(q3)
iqr = q3-q1
print(iqr)
lowerbound = q1 - 1.5*iqr
print(lowerbound)
upperbound = q3 + 1.5*iqr
print(upperbound)
outliers1=[]
for i in range(len(df)):
    if df["Order Amount"][i] < lowerbound or df["Order Amount"][i] > upperbound:
        outliers1.append(df["Order"][i])
print(outliers1)


