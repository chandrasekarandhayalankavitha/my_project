import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv(".github/week13/diabetes_dataset_with_missing.csv.xls")

print(df.isnull().sum())
print(df.head(10))
cols = ['glucose', 'bmi', 'age', 'insulin', 'blood_pressure']
df[cols] = df[cols].fillna(df[cols].median())
print(df.isnull().sum())

q1 = np.percentile(df[cols],25,axis=0)
print(q1)
q3 = np.percentile(df[cols],75,axis=0)
print(q3)
iqr = q3-q1
print(iqr)
lowerbound = q1 - 1.5*iqr
print(lowerbound)
upperbound = q3 + 1.5*iqr
print(upperbound)

outliers = ((df[cols] < lowerbound) | (df[cols] > upperbound))
print(outliers.sum())
print(df[cols].skew())

x = df[cols]
y = df['diabetes']
xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size=0.2,random_state=10)
scaler = StandardScaler()
xtrainscaled = scaler.fit_transform(xtrain)
xtestscaled = scaler.transform(xtest) 

model = LogisticRegression(class_weight='balanced',random_state=42)
model.fit(xtrainscaled, ytrain)
ypred = model.predict(xtestscaled) 

print("Accuracy:", accuracy_score(ytest, ypred))
print("Precision:", precision_score(ytest, ypred))
print("Recall:", recall_score(ytest, ypred))
print("F1 Score:", f1_score(ytest, ypred))