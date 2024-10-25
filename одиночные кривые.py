import matplotlib.pyplot as plt
import numpy as np

# Новые точки данных для размера и времени
sizes = np.array([1000, 6000, 11000, 16000, 21000, 26000, 31000, 36000, 41000, 46000])
times_sorted = np.array([0.000730, 0.003657, 0.014846, 0.013773, 0.021192, 0.032219, 0.023579, 0.052081, 0.051703, 0.051987])

# Создание фигуры и оси для графика
plt.figure(figsize=(10, 6))

# Подгонка и построение полиномиальной кривой для одного набора данных (Sorted)
coeffs = np.polyfit(sizes, times_sorted, 2)  # Подгонка квадратичного полинома (степень 2)
poly = np.poly1d(coeffs)
plt.plot(sizes, poly(sizes), color='blue', label='Random', linewidth=2)

# Построение точек данных
plt.scatter(sizes, times_sorted, color='blue', edgecolors='black')

# Добавление подписей и заголовка
plt.xlabel("Размер массива")
plt.ylabel("Время (секунды)")
plt.title("Время выполнения сортировки (Sorted)")
plt.legend()
plt.grid(True)

# Отображение графика
plt.show()
