import pandas as pd
import numpy as np

data = [20, 30, None, 20, 50, None, 30]
df = pd.Series(data)
print(df.isnull().sum())
print(df.isnull()[0:-1])
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
print(df)
#1. Total runtime of entire show
print(df.sum())
#2. Episodes greater than 50 minutes
print(df[df > 50])
#3. Episodes less than 48 minutes
print(df[df < 48])
#4. Max & Min episode time
print(df.max())
print(df.min())
#5. Which episodes are longest / shortest
print("5a",df.idxmax()+1)
print("5b",df.idxmin()+1)
#6. How many episodes are exactly 47 minutes?
print(df[df == 47].count())
#7. Episodes between 45 and 50 mins
print(df[(df > 45) & (df < 50)])
#8. Convert total runtime to hours & minutes
total_minutes = df.sum()
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"Total runtime: {hours} hours and {minutes} minutes")
#9. Which season has more long episodes (>50 mins)?