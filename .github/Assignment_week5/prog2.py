
import pandas as pd
import numpy as np
data = {"Breaking Bad": 12.5,"Dark": 8.0,"Money Heist": 15.2,"Friends": 6.3}
df = pd.Series(data)
print(df.sort_values(ascending=True))#value
print(df.sort_index(ascending=True))#key
new = {"Dark":8.0}
df = pd.concat([df, pd.Series(new)])
print(df)
df.drop_duplicates(inplace=True)
print(df)
