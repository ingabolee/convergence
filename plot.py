import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
 
# Dataset
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([38545,271155,10366,46329,23132,231651,7188,352105,19528])

plt.bar(range(len(x)), y)
plt.title("A graph of where recursive products of digits upto 1000000 converge")
plt.xlabel("digits")

plt.ylabel("frequency") 

plt.xticks(range(len(x)), x)

plt.show()


#Upto 10,000,000
# 1:  413435 
# 2:  2620040 
# 3:  63911
# 4:  382410
# 5:  165550
# 6:  2349105
# 7:  71267
# 8:  3700992
# 9:  233289