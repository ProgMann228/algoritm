import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Новые данные
sizes = np.array([1000, 6000, 11000, 16000, 21000, 26000, 31000, 36000, 41000, 46000])
sorted_times = np.array([0.000044, 0.000728, 0.001307, 0.002536, 0.004360, 0.006638, 0.010228, 0.013369, 0.018279, 0.024498])
sorted_90_10_times = np.array([0.001084, 0.040491, 0.098589, 0.220762, 0.368132, 0.562423, 0.965386, 1.142505, 1.624122, 2.319250])
reverse_sorted_times = np.array([0.012402, 0.491551, 1.158224, 2.286462, 3.876089, 5.917205, 8.840031, 11.971832, 16.869233, 22.467402])
random_times = np.array([0.004777, 0.219250, 0.727681, 1.187041, 1.929190, 3.015553, 4.371166, 6.687860, 7.668428, 10.760279])

# Функция для аппроксимации (например, квадратичная)
def approx_func(x, a, b, c):
    return a * x**2 + b * x + c

# Аппроксимация данных для каждой серии
popt_sorted, _ = curve_fit(approx_func, sizes, sorted_times)
popt_sorted_90_10, _ = curve_fit(approx_func, sizes, sorted_90_10_times)
popt_reverse_sorted, _ = curve_fit(approx_func, sizes, reverse_sorted_times)
popt_random, _ = curve_fit(approx_func, sizes, random_times)

# Создаем график
plt.figure(figsize=(8, 6))
x_fit = np.linspace(1000, 46000, 400)

# Плотируем исходные данные и аппроксимированные кривые
plt.plot(sizes, sorted_times, 'ro', markersize=4)
plt.plot(x_fit, approx_func(x_fit, *popt_sorted), 'b-', label='Sorted')

plt.plot(sizes, sorted_90_10_times, 'go', markersize=4)
plt.plot(x_fit, approx_func(x_fit, *popt_sorted_90_10), 'g-', label='Sorted 90/10 ')

plt.plot(sizes, reverse_sorted_times, 'co',  markersize=4)
plt.plot(x_fit, approx_func(x_fit, *popt_reverse_sorted), 'c-', label='Revers Sorted')

plt.plot(sizes, random_times, 'mo', markersize=4)
plt.plot(x_fit, approx_func(x_fit, *popt_random), 'm-', label='Random')

# Настройка графика
plt.xlabel('Размер массива')
plt.ylabel('Время (секунды)')
plt.title('Время выполнения сортировки для разных случаев')
plt.legend()
plt.grid(True)

# Показываем график
plt.show()
