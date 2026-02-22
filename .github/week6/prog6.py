import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv(".github/week6/monthly_budget_march2025.csv.xls")
plt.pie(df["Amount_USD"], labels=df["Category"], autopct='%1d%%', startangle=90, shadow=True)
plt.title("Monthly Budget Distribution - March 2025")
plt.show()