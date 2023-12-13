import numpy as np
import matplotlib.pyplot as plt

data1 = [i for i in range(0, 355, 10)]
data2 = [0, 92.8, 187.1, 287.6, 363.2, 453.2, 636.7, 879.2, 923.6, 1128.8, 1190.9, 1134, 1086.4, 1044,
         1003.6, 968.1, 934.2, 908.3, 912, 1063.8, 1228, 1421.5, 1523.7, 1725.1,
         1931.5, 2163.2, 2263.4, 2263.9, 2264.3, 2264.6, 2264.9, 2265.2, 2265.4, 2265.8, 2266.2, 2266.7,
         ]

print(len(data2))
x = np.linspace(0, 340) # время
fig, ax = plt.subplots()

ax.plot(data1, data2)
ax.grid()

ax.set_xlabel('время (с)')
ax.set_ylabel('скорость (м/c)')


plt.show()