import matplotlib.pyplot as plt
import numpy as np

# New data points for sizes and times
sizes = np.array([1000, 6000, 11000, 16000, 21000, 26000, 31000, 36000, 41000, 46000])
times_sorted = np.array([0.016089, 0.326454, 0.888784, 1.879576, 3.214119, 4.884777, 7.027735, 9.167344, 11.194292, 16.499976])
times_sorted_90_10 = np.array([0.009146, 0.433523, 0.684522, 1.914693, 3.373422, 4.790649, 8.457954, 9.165630, 11.713818, 14.464951])
times_reverse_sorted = np.array([0.013097, 0.369454, 0.857169, 1.827497, 2.997831, 5.440546, 7.533626, 9.554477, 11.792752, 14.678825])
times_random = np.array([0.021363, 0.380876, 0.908011, 1.817939, 3.432014, 6.183127, 6.803426, 9.160778, 12.150838, 14.460276])

# Create a figure and axis for the plot
plt.figure(figsize=(10, 6))

# Fit and plot the polynomial curves for each time set to show approximate trends
for times, label, color in zip(
    [times_sorted, times_sorted_90_10, times_reverse_sorted, times_random],
    ["Sorted", "Sorted 90/10", "Revers Sorted", "Random"],
    ['blue', 'green', 'red', 'purple']
):
    coeffs = np.polyfit(sizes, times, 2)  # Fit a quadratic polynomial (degree 2)
    poly = np.poly1d(coeffs)
    plt.plot(sizes, poly(sizes), color=color, label=label, linewidth=2)
    plt.scatter(sizes, times, color=color, edgecolors='black')  # Plot the actual data points

# Add labels and title
plt.xlabel("Размер массива")
plt.ylabel("Время (секунды)")
plt.title("Время выполнения сортировки")
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
