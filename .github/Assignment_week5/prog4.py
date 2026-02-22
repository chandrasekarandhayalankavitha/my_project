import pandas as pd
import numpy as np

data = [20, 30, None, 20, 50, None, 30]
df = pd.Series(data)
print(df.isnull().sum())
print(df.isnull()[0:-1])
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
print(df)


with open("file.csv", "r") as f:
    df = pd.read_csv(f) 