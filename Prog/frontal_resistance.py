import numpy as np
import matplotlib.pyplot as plt
import json 
import math

with open("data.json") as file_in:
    data = json.load(file_in)

#Константы
S = 25 * math.pi # Характерная площадь, м**2
R = 1.2 # Плотность среды, кг/м**3
K = 0.5 # Безразмерный коэффициент C для конуса 

#Лобовое сопротивление
frontal_resistance = []

for i in data['speed']:
    frontal_resistance.append(K * S * (R * i**2) / 2) 
    print(K * S * (R * i**2) / 2)
#Построение графика
fig, ax = plt.subplots()

ax.plot(data['speed'], frontal_resistance)

ax.set_title('Сила лобового сопротивления от скорости ракеты')

ax.set_xlabel('Скорость ракеты, м/с')
ax.set_ylabel('Сила лобового сопротивления, Н * 10^8')


plt.show()
