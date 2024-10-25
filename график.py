import numpy as np
import matplotlib.pyplot as plt

# Определяем функцию f(x), например O(n log n)
def f(x):
    return x **(5/4)

# Генерируем значения для оси X (размер массива)
x_values = np.linspace(1, 50000, 100)  # от 1 до 50000

# Вычисляем значения для оси Y (значения функции сложности)
y_values = f(x_values)

# Построение графика
plt.plot(x_values, y_values, label='$O(n^(5/4))$', color='blue')

# Настройка графика
plt.title('График функции сложности $O(n^(5/4))$')
plt.xlabel('Размер массива (n)')
plt.ylabel('Сложность')
plt.legend()

# Отображение графика
plt.show()
