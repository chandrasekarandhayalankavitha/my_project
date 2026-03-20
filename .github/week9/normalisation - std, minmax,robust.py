
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
import numpy as np 

data = [[1, 2],
        [3, 4],
        [5, 6],
        [7,8],
        [9,10]]

scaler = StandardScaler()
scaled = scaler.fit_transform(data)
print("original data :", data)
print("scaled data :",scaled)

scaler = MinMaxScaler()
scaled = scaler.fit_transform(data)
print("original data :", data)
print("scaled data :",scaled)

scaler = RobustScaler()
scaled = scaler.fit_transform(data)
print("original data :", data)
print("scaled data :",scaled)