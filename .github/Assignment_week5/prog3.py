
import pandas as pd
import numpy as np

data1 = {"Breaking Bad": 6.0,"Dark": 4.0,"Money Heist": 7.5}
data2 = {"Friends": 6.5,"Game of Thrones": 4.0,"The Office": 7.7}
df1 = pd.Series(data1)
df2 = pd.Series(data2)
print("sum",df1.add(df2))
print("sub",df1.sub(df2))
print("mul",df1.mul(df2))
print("div",df1.div(df2))
df = pd.concat([df1, df2])
print(df)