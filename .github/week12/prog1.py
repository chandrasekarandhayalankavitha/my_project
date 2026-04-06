import pandas as pd
import numpy as pd
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
le.fit(["Red","Blue","Green","Yellow","Pink"])
print(le.transform(["Red","Blue","Green","Yellow","Pink"]))
print(le.inverse_transform([0,1,2,3,4]))