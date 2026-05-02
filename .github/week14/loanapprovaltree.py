import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
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

feature_names = x.columns.tolist()

x = np.array(x)
y = np.array(y)

model = DecisionTreeClassifier(criterion="entropy")
model.fit(x, y)

plt.figure(figsize=(20, 12))   
plot_tree(
    model,
    feature_names=feature_names,
    class_names=ledict['Approved'].classes_,
    filled=True,
    fontsize=12
)
plt.show()

uinput = ["Employed", "Good", "Medium", "Few"]
uinputencoded = np.array([[
    ledict['Employment'].transform([uinput[0]])[0],
    ledict['CreditScore'].transform([uinput[1]])[0],
    ledict['LoanAmount'].transform([uinput[2]])[0],
    ledict['Dependents'].transform([uinput[3]])[0]
]])

prediction = model.predict(uinputencoded)
result = ledict['Approved'].inverse_transform(prediction)
print(result)