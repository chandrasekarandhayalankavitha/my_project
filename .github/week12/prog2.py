import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(".github/week12/sales_data_logistic.csv.xls")
le = LabelEncoder()
transformedCT = le.fit_transform(df["CardType"])

x = df[["Total Amount"]]
y = transformedCT
xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size=0.2,random_state=10)
model = LogisticRegression(class_weight='balanced',random_state=42)
model.fit(xtrain,ytrain)

uinput = int(input("Enter total amount"))
Tuinput = [[uinput]]
pred = model.predict(Tuinput)
print(le.inverse_transform(pred))