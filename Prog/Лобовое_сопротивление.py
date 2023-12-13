import numpy as np
import math
import matplotlib.pyplot as plt

#Константы
S = 25 * math.pi # Характерная площадь, м**2
R = 1.2 # Плотность среды, кг/м**3
K = 0.5 # Безразмерный коэффициент C для конуса 

#Значения переменных
x = np.linspace(0, 3500) #Cкорость ракеты
y = K * S * (R * x**2) / 2 #Лобовое сопротивление

#Построение графика
fig, ax = plt.subplots()

ax.plot(x, y)
ax.grid()

ax.set_xlabel('Скорость ракеты, м/с')
ax.set_ylabel('Сила лобового сопротивления, Н')


plt.show()