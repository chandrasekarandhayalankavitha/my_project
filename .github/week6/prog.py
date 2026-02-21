
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(".github/folder/Calorie_Tracking_Dataset.xls")

df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")
df = df.sort_values("Date")

plt.figure()
plt.plot(df["Date"], df["Daily Weight (kg)"], marker='o')
plt.xlabel("Date")
plt.ylabel("Daily Weight (kg)")
plt.title("Daily Weight Trend (January 2026)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
plt.bar(df["Date"].dt.strftime("%d-%m"), df["Total Calorie Intake (kcal)"])
plt.xlabel("Date")
plt.ylabel("Total Calorie Intake (kcal)")
plt.title("Daily Calorie Intake (January 2026)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
