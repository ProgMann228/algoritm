import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data for size and times
size = np.array([1000, 6000, 11000, 16000, 21000, 26000, 31000, 36000, 41000, 46000])
times_sorted = np.array([0.009630, 0.082046, 0.139923, 0.248425, 0.275763, 0.306858, 0.345045, 0.438263, 0.504914, 0.548714])
times_sorted_90_10 = np.array([0.000292, 0.002472, 0.005501, 0.011192, 0.013344, 0.015856, 0.020491, 0.016963, 0.022932, 0.031304])
times_reverse_sorted = np.array([0.005758, 0.087127, 0.197101, 0.505440, 0.380635, 0.382018, 0.446853, 0.575046, 0.610230, 0.675806])
times_random = np.array([0.000229, 0.003110, 0.003505, 0.009156, 0.009967, 0.008747, 0.010375, 0.014457, 0.016345, 0.017482])

# Fit function for O(n log n)
def fit_func(n, a):
    return a * n * np.log(n)

# Fit curves for each data set
popt_sorted, _ = curve_fit(fit_func, size, times_sorted)
popt_sorted_90_10, _ = curve_fit(fit_func, size, times_sorted_90_10)
popt_reverse_sorted, _ = curve_fit(fit_func, size, times_reverse_sorted)
popt_random, _ = curve_fit(fit_func, size, times_random)

# Generate smooth lines for the fit
size_fit = np.linspace(size.min(), size.max(), 100)
times_fit_sorted = fit_func(size_fit, *popt_sorted)
times_fit_sorted_90_10 = fit_func(size_fit, *popt_sorted_90_10)
times_fit_reverse_sorted = fit_func(size_fit, *popt_reverse_sorted)
times_fit_random = fit_func(size_fit, *popt_random)

# Plotting the data and fits
plt.figure(figsize=(10, 6))
plt.plot(size, times_sorted, 'ro',  markersize=5)
plt.plot(size_fit, times_fit_sorted, 'r-', label='Sorted')

plt.plot(size, times_sorted_90_10, 'bo', markersize=5)
plt.plot(size_fit, times_fit_sorted_90_10, 'b-', label='Sorted 90/10')

plt.plot(size, times_reverse_sorted, 'go', markersize=5)
plt.plot(size_fit, times_fit_reverse_sorted, 'g-', label='Reverse Sorted')

plt.plot(size, times_random, 'mo', markersize=5)
plt.plot(size_fit, times_fit_random, 'm-', label='Random')

plt.xlabel('Size')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of Sorting Algorithms')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
