import numpy as np
import matplotlib.pyplot as plt
import math

# Определяем функции сложности для различных алгоритмов сортировки
def select_sort(x):
    return x**2  # O(n^2)

def insert_sort(x):
    return x**2  # O(n^2)

def bubble_sort(x):
    return x**2  # O(n^2)

def merge_sort(x):
    return x * np.log(x)  # O(n log n)

def quick_sort(x):
    return x * np.log(x)  # O(n log n)

def shell_sort(x):
    return x**(3/2)  # O(n^(3/2))

def shell_sort_hibbard(x):
    return x**(5/4)  # O(n^(5/4))

def shell_sort_pratt(x):
    return x * np.log(x)**2  # O(n log n)

def heap_sort(x):
    return x * np.log(x)  # O(n log n)

# Генерируем значения для оси X (размер массива)
x_values = np.linspace(1, 10000, 100)

# Построение графика всех функций сложности
def plot_sorting_complexity_curves():
    plt.figure(figsize=(10, 8))

    # Построение всех 9 функций сложности
    plt.plot(x_values, select_sort(x_values), label='Select Sort $O(n^2)$', color='blue')
    plt.plot(x_values, insert_sort(x_values), label='Insert Sort $O(n^2)$', color='green')
    plt.plot(x_values, bubble_sort(x_values), label='Bubble Sort $O(n^2)$', color='red')
    plt.plot(x_values, merge_sort(x_values), label='Merge Sort $O(n \log n)$', color='purple')
    plt.plot(x_values, quick_sort(x_values), label='Quick Sort $O(n \log n)$', color='orange')
    plt.plot(x_values, shell_sort(x_values), label='Shell Sort $O(n^{3/2})$', color='brown')
    plt.plot(x_values, shell_sort_hibbard(x_values), label='Shell Sort (Hibbard) $O(n^{5/4})$', color='pink')
    plt.plot(x_values, shell_sort_pratt(x_values), label='Shell Sort (Pratt) $O(n \log^2 n)$', color='gray')
    plt.plot(x_values, heap_sort(x_values), label='Heap Sort $O(n \log n)$', color='cyan')

    # Настройка графика
    plt.title('Графики сложности сортировок')
    plt.xlabel('Размер массива (n)')
    plt.ylabel('Сложность')
    plt.yscale('log')  # Логарифмическая шкала для лучшей визуализации
    plt.legend()

    # Отображение графика
    plt.show()

# Вызов функции для построения графика
plot_sorting_complexity_curves()
