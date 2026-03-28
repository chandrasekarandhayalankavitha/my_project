import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

df = pd.read_csv(".github/week10/house_price_dataset.csv.xls")
x = np.array(df["house_size_sqft"]).reshape(-1,1)
y = np.array(df["price_lakhs"])

model = LinearRegression()
model.fit(x,y)

slope = model.coef_[0]
intercept = model.intercept_
ypred = model.predict(x)
mse = mean_squared_error(y,ypred)
r2 = r2_score(y,ypred)

print("slope", slope)
print("intercept", intercept)
print("ypred", ypred)
print("MSE", mse)
print("r2",r2)

userinput = int(input("enter sqft"))
formattedui = np.array(userinput).reshape(-1,1)
ypred = model.predict(formattedui)
print("ypred for user inp",ypred)


