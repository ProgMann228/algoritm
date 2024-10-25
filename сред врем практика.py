import numpy as np
import matplotlib.pyplot as plt

# Примерные данные для разных сортировок
x_values = np.array([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])

# Примерные времена выполнения для разных сортировок
#select_sort_times = [0.021363, 0.380876, 0.908011, 1.817939, 3.432014, 6.183127, 6.803426, 9.160778, 12.150838, 14.460276]
#insert_sort_times = [0.004777, 0.219250, 0.727681, 1.187041, 1.929190, 3.015553, 4.371166, 6.687860, 7.668428, 10.760279]
#bubble_sort_times = [0.027179, 1.591292, 3.152204, 6.234852, 10.447068, 16.040738, 24.795687, 38.032569, 44.025937,
        #        57.117807]
merge_sort_times = [0.004288, 0.036606, 0.039245, 0.055271, 0.074365, 0.278327, 0.178668, 0.147828, 0.137448, 0.234085]
quick_sort_times = [0.000229, 0.003110, 0.003505, 0.009156, 0.009967, 0.008747, 0.010375, 0.014457, 0.016345, 0.017482]
#shell_sort_times = [0.000542, 0.003221, 0.007271, 0.016820, 0.036144, 0.035915, 0.029478, 0.040986, 0.064132, 0.056732]
#shell_sort_hibbard_times = [0.001726, 0.018034, 0.013841, 0.033020, 0.036911, 0.036318, 0.046446, 0.138549, 0.079724, 0.071832]
shell_sort_pratt_times = [0.001701, 0.013908, 0.031453, 0.043204, 0.047762, 0.090749, 0.113194, 0.094905, 0.104733, 0.132987]
heap_sort_times = [0.000730, 0.003657, 0.014846, 0.013773, 0.021192, 0.032219, 0.023579, 0.052081, 0.051703, 0.051987]


# Функция для построения регрессионных кривых
def plot_regression_curve(x, y, label, color, degree=2):
    # Полиномиальная регрессия для подгонки кривой
    poly_coeff = np.polyfit(x, y, degree)
    poly_eq = np.poly1d(poly_coeff)

    # Генерация x-значений для гладкой кривой
    x_smooth = np.linspace(min(x), max(x), 500)
    y_smooth = poly_eq(x_smooth)

    # Построение регрессионной кривой
    plt.plot(x_smooth, y_smooth, label=label, color=color)


# Построение регрессионных кривых
def plot_sorting_regression():
    plt.figure(figsize=(10, 8))

    # Построение регрессионных кривых для каждого алгоритма сортировки
    #plot_regression_curve(x_values, select_sort_times, 'Select Sort', 'blue', degree=2)
    #plot_regression_curve(x_values, insert_sort_times, 'Insert Sort', 'green', degree=2)
    #plot_regression_curve(x_values, bubble_sort_times, 'Bubble Sort', 'red', degree=2)
    plot_regression_curve(x_values, merge_sort_times, 'Merge Sort', 'purple', degree=2)
    plot_regression_curve(x_values, quick_sort_times, 'Quick Sort', 'orange', degree=2)
    #plot_regression_curve(x_values, shell_sort_times, 'Shell Sort', 'brown', degree=2)
    #plot_regression_curve(x_values, shell_sort_hibbard_times, 'Shell Sort (Hibbard)', 'pink', degree=2)
    plot_regression_curve(x_values, shell_sort_pratt_times, 'Shell Sort (Pratt)', 'gray', degree=2)
    plot_regression_curve(x_values, heap_sort_times, 'Heap Sort', 'cyan', degree=2)

    # Настройки графика
    plt.title('Регрессионные кривые времени выполнения сортировок')
    plt.xlabel('Размер массива (n)')
    plt.ylabel('Время выполнения (с)')
    plt.legend()

    # Отображение графика
    plt.show()


# Вызов функции для построения графика
plot_sorting_regression()
