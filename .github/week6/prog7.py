import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.arange(1, 6) #[1 2 3 4 5]
y1 = x * 2 #[2 4 6 8 10]
y2 = x ** 2 #[1 4 9 16 25]
y3 = np.random.randint(1, 10, size=5) #Eg : [3,4,5,8,9]
y4 = np.random.randint(10, 20, size=5) #Eg : [13,14,15,18,19]

fig, axs = plt.subplots(2,2,figsize=(10,8))

axs[0,0].plot(x,y1,marker='o')
axs[0,0].set_title('Line Plot')

axs[0,1].bar(x,y2, color = 'orange', edgecolor = 'black')
axs[0,1].set_title('Bar Plot')

axs[1,0].scatter(x,y3, color = 'green', edgecolor = 'black')
axs[1,0].set_title('Scatter Plot')

axs[1,1].pie(y4, labels = x, autopct = '%1d%%', startangle = 90, shadow = True)
axs[1,1].set_title('Pie Chart')

plt.show()
