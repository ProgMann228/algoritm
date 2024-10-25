import matplotlib.pyplot as plt
import numpy as np

# Данные
sizes = [1000, 6000, 11000, 16000, 21000, 26000, 31000, 36000, 41000, 46000]
sorted_times = [0.020285, 0.600009, 2.080599, 4.219193, 7.117762, 12.107055, 16.819767, 23.267277, 29.367486, 37.200036]
sorted_90_10_times = [0.019024, 0.701206, 2.259987, 4.488781, 7.817266, 13.461636, 18.357954, 34.936720, 31.919679,
                      40.335902]
reverse_sorted_times = [0.028436, 1.439566, 3.321667, 7.154694, 12.264148, 19.962136, 28.786903, 55.969731, 50.827831,
                        63.745582]
random_times = [0.027179, 1.591292, 3.152204, 6.234852, 10.447068, 16.040738, 24.795687, 38.032569, 44.025937,
                57.117807]

# Создание графика
plt.figure(figsize=(10, 6))

# Построение точек и аппроксимирующей кривой для каждой серии данных
for times, label, color in [
    (sorted_times, 'Sorted', 'blue'),
    (sorted_90_10_times, 'Sorted 90/10', 'green'),
    (reverse_sorted_times, 'Reverse Sorted', 'red'),
    (random_times, 'Random', 'purple')
]:
    # Аппроксимация кривой полиномиальной функции 2-й степени
    coefficients = np.polyfit(sizes, times, 2)
    poly = np.poly1d(coefficients)
    approx_times = poly(sizes)

    # Рисуем точки и кривую
    plt.plot(sizes, approx_times, label=f'{label} ', color=color)
    plt.scatter(sizes, times, color=color, s=40, alpha=0.7)

# Настройки графика
plt.title('Время выполнения сортировки')
plt.xlabel('Размер массива')
plt.ylabel('Время (секунды)')
plt.grid(True)
plt.legend(loc='upper left')

# Показать график
plt.tight_layout()
plt.show()
