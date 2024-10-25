import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data for size and times
size = np.array([1000, 6000, 11000, 16000, 21000, 26000, 31000, 36000, 41000, 46000])
times_sorted = np.array([0.001104, 0.010564, 0.027499, 0.039809, 0.101804, 0.070779, 0.113490, 0.088226, 0.093712, 0.110191])
times_sorted_90_10 = np.array([0.001433, 0.012373, 0.023890, 0.058419, 0.142840, 0.106866, 0.112789, 0.091266, 0.102067, 0.113058])
times_reverse_sorted = np.array([0.001395, 0.009989, 0.023441, 0.051294, 0.051296, 0.083405, 0.089877, 0.095385, 0.094725, 0.114368])
times_random = np.array([0.001701, 0.013908, 0.031453, 0.043204, 0.047762, 0.090749, 0.113194, 0.094905, 0.104733, 0.132987])


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
