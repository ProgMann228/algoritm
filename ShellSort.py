import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data for size and times
size = np.array([1000, 6000, 11000, 16000, 21000, 26000, 31000, 36000, 41000, 46000])
times_sorted = np.array([0.000188, 0.001203, 0.003930, 0.004973, 0.008713, 0.012016, 0.008287, 0.021181, 0.017371, 0.023558])
times_sorted_90_10 = np.array([0.000415, 0.002198, 0.005048, 0.008429, 0.015050, 0.030715, 0.019201, 0.099514, 0.039572, 0.035505])
times_reverse_sorted = np.array([0.000391, 0.001934, 0.003853, 0.007896, 0.013980, 0.019087, 0.015198, 0.246373, 0.020157, 0.028533])
times_random = np.array([0.000542, 0.003221, 0.007271, 0.016820, 0.036144, 0.035915, 0.029478, 0.040986, 0.064132, 0.056732])

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
