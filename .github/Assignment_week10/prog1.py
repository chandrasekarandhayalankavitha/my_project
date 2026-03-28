
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from scipy.stats import zscore
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(".github/Assignment_week10/simple_linear_regression_500_rows (1).csv")
print(df.head())
print(df.info())
print(df[df['Price'].isnull()].index)
plt.scatter(df['Area'], df['Price'])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price")
plt.show()

df['Price'] = df['Price'].fillna(df['Price'].mean())
zscores = zscore(df[['Area', 'Price']])
dfclean = df[((zscores > -3) & (zscores < 3)).all(axis=1)]
dfclean = dfclean.reset_index(drop=True)

data = dfclean[['Area']]
scaler = StandardScaler()
scaled = scaler.fit_transform(data)
scaleddf = pd.DataFrame(scaled, columns=data.columns)
print("original data :", data.head(10))
print("scaled data :",scaleddf.head(10))
print("mean:",scaleddf.mean())
print("std:",scaleddf.std())
dfclean['Area'] = scaleddf['Area']

x = np.array(dfclean["Area"]).reshape(-1, 1)
y = np.array(dfclean["Price"])
model = LinearRegression()
model.fit(x, y)
slope = model.coef_[0]       
intercept = model.intercept_     
ypred = model.predict(x)
mse = mean_squared_error(y, ypred)
r2 = r2_score(y, ypred)
print("slope", slope)
print("intercept", intercept)
print("ypred", ypred)
print("MSE", mse)
print("r2",r2)
