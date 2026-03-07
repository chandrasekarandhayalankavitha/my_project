
import pandas as pd
import numpy as np

df = pd.read_csv(".github/Assignment_week7/Employee_Missing_Data_100_Rows.csv")
print(df.isna().sum())
df1 = df.dropna()
print(df1.isna().sum())
df2 = df.dropna(how='all')
print(df2.isna().sum())
df3 = df.dropna(thresh=3)
print(df3.count)
df3["Age"].fillna(df["Age"].mean(), inplace=True)
df3["Salary"].fillna(df["Salary"].median(), inplace=True)
df3["PerformanceScore"].fillna(0, inplace=True)
print(df3.head())
dff = df.ffill()
print(dff.head())
dfb = df.bfill()
print(dfb.head())



df3.dropna(axis=1, thresh=4)
df["PerformanceScore"].fillna(df["PerformanceScore"].median(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)
print(df["Salary"].mean())
print(df["Salary"].median())
print(df["Salary"].std())

mean_salary = df["Salary"].mean()
std_salary = df["Salary"].std()

df["Z_score"] = (df["Salary"] - mean_salary) / std_salary

outliers = df[abs(df["Z_score"]) > 2]
print(outliers)