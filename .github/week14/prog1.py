import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np

df1 = pd.read_csv(".github/week14/loan_approval.csv.xls")
df1 = df1.dropna()
df = df1.copy()

ledict = {}
for column in df.columns:
    if df[column].dtype in ['object', 'str']:
        le = LabelEncoder()
        encodedvalues = le.fit_transform(df[column])
        df[column] = encodedvalues
        ledict[column] = le

x = df.drop(['Day', 'Approved'], axis=1)
y = df['Approved']
x = np.array(x)
y = np.array(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print("Accuracy:")
print(accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=ledict['Approved'].classes_))

uinput = ["Employed", "Good", "Medium", "Few"]
uinputencoded = np.array([[
    ledict['Employment'].transform([uinput[0]])[0],
    ledict['CreditScore'].transform([uinput[1]])[0],
    ledict['LoanAmount'].transform([uinput[2]])[0],
    ledict['Dependents'].transform([uinput[3]])[0]
]])

prediction = model.predict(uinputencoded)
result = ledict['Approved'].inverse_transform(prediction)
print("Prediction:",result[0])