import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv(".github/week14/decisiontree.csv.xls")
df = df.dropna(how='all')
df = df.drop('Day', axis=1)

X = df.drop('Play', axis=1)
y = df['Play']

for column in X.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    X[column] = le.fit_transform(X[column])

le_target = LabelEncoder()
y = le_target.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)
rf_classifier.fit(X_train, y_train)

y_pred_test = rf_classifier.predict(X_test)

new_data = pd.DataFrame({
    'Weather': ['Sunny'],
    'Temperature': ['Hot'],
    'Humidity': ['High'],
    'Wind': ['Weak']
})

for column in new_data.columns:
    le = LabelEncoder()
    le.fit(df[column])
    new_data[column] = le.transform(new_data[column])

new_prediction = rf_classifier.predict(new_data)
new_prediction_label = le_target.inverse_transform(new_prediction)[0]

print(f"New Data Prediction: {new_prediction_label}\n")
print(f"Test Accuracy: {accuracy_score(y_test, y_pred_test):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred_test, target_names=le_target.classes_))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_test))