import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

stud_data = {
    "study_hrs" : [1,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10],
    "marks" : [35,40,42,48,50,55,58,62,65,70,72,75,78,82,85,88,90,93]
}
df = pd.DataFrame(stud_data)
plt.scatter(df['study_hrs'], df['marks'])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Positive Correlation")
plt.show()
print(df.corr())