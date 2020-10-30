import numpy as np
import matplotlib.pyplot as plt


my_data = np.random.normal(100.0,20.0,10000)


print (my_data.var())
print (my_data.std())
plt.hist(my_data,50)
plt.show()