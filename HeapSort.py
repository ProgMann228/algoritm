import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data for size and times
size = np.array([1000, 6000, 11000, 16000, 21000, 26000, 31000, 36000, 41000, 46000])
times_sorted = np.array([0.000526, 0.003693, 0.007514, 0.011677, 0.021988, 0.021798, 0.039099, 0.053165, 0.043909, 0.045770])
times_sorted_90_10 = np.array([0.000675, 0.004320, 0.009114, 0.017116, 0.021900, 0.021354, 0.036105, 0.046233, 0.047460, 0.051646])
times_reverse_sorted = np.array([0.000666, 0.004051, 0.015087, 0.011544, 0.022808, 0.025665, 0.024532, 0.058305, 0.038624, 0.045892])
times_random = np.array([0.000730, 0.003657, 0.014846, 0.013773, 0.021192, 0.032219, 0.023579, 0.052081, 0.051703, 0.051987])


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
