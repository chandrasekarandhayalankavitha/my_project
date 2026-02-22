import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = [10, 20, 20, 30, 40, 40, 40, 50, 60, 70, 80, 80, 90]
plt.hist(data,bins=6,histtype="stepfilled",alpha=0.7,orientation="vertical",edgecolor="black")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Styled Histogram")
plt.show()

