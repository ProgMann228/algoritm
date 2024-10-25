import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data for size and times
size = np.array([1000, 6000, 11000, 16000, 21000, 26000, 31000, 36000, 41000, 46000])
times_sorted = np.array([0.000361, 0.016106, 0.004343, 0.015506, 0.012596, 0.012585, 0.023050, 0.026757, 0.027594, 0.027359])
times_sorted_90_10 = np.array([0.000707, 0.013666, 0.010212, 0.021317, 0.024361, 0.031915, 0.046306, 0.060104, 0.048218, 0.040391])
times_reverse_sorted = np.array([0.000623, 0.008419, 0.006772, 0.022249, 0.019870, 0.027367, 0.023782, 0.039493, 0.037742, 0.030228])
times_random = np.array([0.001726, 0.018034, 0.013841, 0.033020, 0.036911, 0.036318, 0.046446, 0.138549, 0.079724, 0.071832])


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
