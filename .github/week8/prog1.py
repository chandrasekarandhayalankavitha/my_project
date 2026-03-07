import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Math": [85, 70, 95, 60, 82, 74, 91, 66, 88, 79],
    "Science": [78, 65, 88, 55, 80, 69, 90, 61, 84, 73],
    "English": [90, 75, 92, 65, 86, 71, 94, 68, 89, 77],
    "History": [88, 72, 91, 58, 83, 70, 93, 64, 87, 76],
    "Geography": [84, 68, 90, 62, 81, 66, 92, 65, 85, 74],
    "Computer": [95, 78, 98, 70, 92, 80, 99, 75, 96, 82],
    "Physics": [76, 60, 89, 52, 74, 63, 90, 58, 80, 67],
    "Chemistry": [79, 62, 87, 50, 77, 64, 91, 57, 82, 69],
    "Biology": [81, 64, 90, 54, 78, 67, 92, 60, 83, 71],
    "Economics": [73, 59, 86, 56, 70, 61, 88, 62, 76, 65],
    "Art": [92, 80, 94, 75, 88, 82, 96, 78, 90, 84],
    "Sports": [89, 76, 93, 72, 85, 79, 95, 74, 88, 81],
    "Hindi": [86, 71, 92, 63, 83, 69, 94, 66, 87, 75],
    "Sanskrit": [80, 66, 88, 60, 78, 64, 90, 62, 82, 70]
}


students = [
    "Sachin",
    "Dhoni",
    "Kohli",
    "Samson",
    "Rohit",
    "Rahul",
    "Hardik",
    "Jadeja",
    "Bumrah",
    "Gill",
]

df = pd.DataFrame(data, index=students)
plt.figure()
sns.heatmap(df,annot=True,cmap="viridis")
plt.title("Performance Heatmap")
plt.tight_layout()
plt.show()
