import matplotlib.pyplot as plt
import numpy as np

# Data tren biaya pipa
slope = [0.1157192, 0.0783067]
intercept = [0.4316551, 0.770037]
big_M = 56.46  # Max flow allowed in a pipeline tCO2/yr
ltrend = 6.86  # Upperbound flow for lower pipeline trend tCO2/yr

# Membuat array untuk jumlah CO2 (dalam MTCO2/tahun)
co2_amounts = np.linspace(0, big_M, 100)  # Menggunakan Big_M sebagai batas atas

# Menghitung biaya untuk setiap tren
costs_1 = slope[0] * co2_amounts + intercept[0]
costs_2 = slope[1] * co2_amounts + intercept[1]

# Membuat grafik
plt.figure(figsize=(10, 5))
plt.plot(co2_amounts, costs_1, label='Tren 1')
plt.plot(co2_amounts, costs_2, label='Tren 2')

# Menandai LTrend pada grafik
plt.axvline(x=ltrend, color='grey', linestyle='--', label='LTrend')

# Menambahkan judul dan label
plt.title('Grafik Tren Biaya Pipa dengan Big_M dan LTrend')
plt.xlabel('Jumlah CO2 (MTCO2/tahun)')
plt.ylabel('Biaya ($M/tahun)')
plt.legend()
plt.grid(True)

# Menampilkan grafik
plt.show()