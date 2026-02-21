
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(".github/folder/ad_spend_vs_sales_revenue.csv.xls")

x = df["Ad_Spend_USD"]
y = df["ROI_Percent"]

plt.figure()
plt.scatter(x, y, s=None, c=None, marker=None, cmap=None, alpha=None, edgecolors=None, label=None)
plt.xlabel("Ad Spend (USD)")
plt.ylabel("ROI (%)")
plt.title("Ad Spend vs ROI")
plt.tight_layout()
plt.show()