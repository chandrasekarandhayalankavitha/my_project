
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 
student_marks = [23, 35, 45, 50, 52, 55, 58, 60, 63, 65,
                 67, 68, 70, 72, 74, 75, 76, 78, 80, 82,
                 83, 85, 88, 90, 92, 95, 98, 61, 73, 77]

plt.hist(student_marks, bins=10)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Marks")
plt.legend(["Marks Distribution"])
plt.show()
