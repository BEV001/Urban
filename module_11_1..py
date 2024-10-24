
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#work with numpy
C = np.zeros(5)
print (C)

#work with pandas
A = pd.Series(np.random.randn(10), index=pd.date_range("24/10/2024", periods=10))
print(A)

#work with mathlotib
figure, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [8, 6, 0, 7])
plt.show()