import numpy as np
import matplotlib.pyplot as plt
import json 

with open("data.json") as file_in:
    data = json.load(file_in)


#Построение графика
fig_speed, ax_speed = plt.subplots()

ax_speed.plot(data['met'], data['speed'])

ax_speed.set_title('Зависимость скорости от времени')

ax_speed.set_xlabel('Время, c')
ax_speed.set_ylabel('Скорость, м/c')

plt.show()
