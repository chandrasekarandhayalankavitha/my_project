
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "speed" : [30,35,40,45,50,55,60,65,70,75,80,85,90,95,100],
    "time" :  [120,110,100,92,85,78,70,65,60,57,55,53,50,48,45]
}
df = pd.DataFrame(data)
plt.scatter(df['speed'], df['time'])
plt.xlabel("Speed")
plt.ylabel("Time Taken")
plt.title("Negative Correlation")
plt.show()
print(df.corr())