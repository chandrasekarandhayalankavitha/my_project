
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler

#part1
#q1
df = pd.read_csv(".github/Assignment_week9/scaling_homework_dataset_100_rows.csv")

#q2 & #q3
print(df.info())
'''
Numerical columns --> EmployeeID, Age, Experience, Salary, PerformanceScore, Bonus
Categorical columns --> Department
'''
#q4 & q5
print(df.head(10))
'''
columns --> 'Age', 'Experience', 'Salary', 'PerformanceScore' needs scaling.
columns --> EmployeeID, Department and Bonus does not require scaling.
EmployeeID --> it is unique entry column used to identify each sample and will not be used in predicitng the target variable
Bonus --> it is the target variable (the value we want to arrive at), so we should scale the required to get the target
and not the target.
Department --> It is a categorical column, we will not be using mathematical functions or any sorts related to
computing the targe value. so it is ignored
'''

#part2
print("Age",df['Age'].describe())
print("Experience",df['Experience'].describe())
print("Salary",df['Salary'].describe())
print("PerformanceScore",df['PerformanceScore'].describe())
print("Bonus",df['Bonus'].describe())

'''
the features are not in the same scale because : 
1. all of them represent different domains
2. age mostly limits between 19 to 59 in terms of work/salary
3. salary is the amount you get as part of your and it progress thorugh age and it has big numbers mostly 5 digit ones
4. performance is marked out of 100, though it might seem close to age, it is not. a person with age of 50 can have
a rating of 60 whereas a person of age 25 can have a rating of 90. it depends on how you perfom, not your age.
5. Experience is the measure of years the same as age and their scale is almost scale that they might not need any scaling.
But there are other features we have which are of different ranges and needs scaling to fit here. So it is better to 
scale every in current scenario.
'''

#part3
data = df.filter(items=["Age", "Experience", "Salary", "PerformanceScore"])
scaler = StandardScaler()
scaled = scaler.fit_transform(data)
scaleddf = pd.DataFrame(scaled, columns=data.columns)
print("original data :", df.head(5))
print("scaled data :",scaleddf.head(5))
print("mean:",scaleddf.mean())
print("std:",scaleddf.std())

#part4
scaler = MinMaxScaler()
scaled = scaler.fit_transform(data)
scaleddf = pd.DataFrame(scaled, columns=data.columns)
print("scaled data :",scaleddf.head(5))
print("mean:",scaleddf.min())
print("std:",scaleddf.max())

#part5
scaler = RobustScaler()
scaled = scaler.fit_transform(data)
scaleddf = pd.DataFrame(scaled, columns=data.columns)
print("scaled data :",scaleddf.head(5))
print("mean:",scaleddf.min())
print("std:",scaleddf.max())
'''
robust uses median, iqr. for that fact it is better for outlier handling as median is the exact middle of the scale
and iqr makes use of 25th and 75th. All falls within place in the bell curve of z-score
'''

#part6
'''
1.	What is feature scaling? 
to align all features to a common scaling, measuring ground
2.	Why do machine learning algorithms require scaling? 
for better modelling
3.	What might happen if Salary values are very large compared to Age? 
the result in this case prediction will be at fault as no proper scaling leads to biased results due to larger values of
salary column. it might actually skip the miss the age factor (essential) due to small values. 
4.	Which scaler would you choose if the dataset contains outliers?
depends on the amount of outliers. 
minimal --> standard or minmax
high --> robust
'''

#bonus
q1 = df["Salary"].quantile(0.25)
q3 = df["Salary"].quantile(0.75)
iqr = q3-q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = df[(df["Salary"]<lower_bound) | (df["Salary"]>upper_bound)]
print(lower_bound)
print(upper_bound)
print(outliers['Salary'])
#i could use any scalar as there is only 2/100 is outlier.