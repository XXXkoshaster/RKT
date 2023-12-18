import numpy as np
import matplotlib.pyplot as plt
import json 

with open("data.json") as file_in:
    data = json.load(file_in)


#Построение графика
fig_speed, ax_speed = plt.subplots()

ax_speed.plot(data['met'], data['altitude'])

ax_speed.set_title('Зависимость высоты от времени')

ax_speed.set_xlabel('Время, c')
ax_speed.set_ylabel('Высота, м * 10^7')

plt.show()