
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

months = ['January', 'February', 'March', 'April']
product_a_sales = [120, 150, 170, 200]
product_b_sales = [80, 100, 90, 40] 

plt.bar(months,product_a_sales,color="blue")
plt.bar(months,product_b_sales,bottom = product_a_sales,color="orange")
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Data')
plt.legend(['Product A', 'Product B'])
plt.show()
