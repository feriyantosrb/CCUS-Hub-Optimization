import numpy as np
import matplotlib.pyplot as plt

# Data slope dan intercept
slope = [0.1157192, 0.0783067]  # Slope (kemiringan)
intercept = [0.4316551, 0.770037]  # Intercept

# Fungsi untuk menghitung biaya pembangunan pipa berdasarkan volume CO2
def calculate_pipeline_build_cost(volume_CO2, slope, intercept):
    return slope * volume_CO2 + intercept

# Volume CO2 yang dipindahkan (dalam satuan MtCO2/year)
volume_CO2 = np.linspace(0, 100, 100)  # Di sini, kita menggunakan rentang dari 0 hingga 100 MtCO2/year

# Membuat grafik
plt.figure(figsize=(10, 6))

# Plot untuk setiap tren biaya
for i in range(len(slope)):
    plt.plot(volume_CO2, calculate_pipeline_build_cost(volume_CO2, slope[i], intercept[i]), label=f'Trend {i+1}')

plt.title('Pipeline Build Cost vs CO2 Volume')
plt.xlabel('CO2 Volume (MtCO2/year)')
plt.ylabel('Pipeline Build Cost ($M/km)')
plt.legend()
plt.grid(True)

# # Mengatur sumbu y dalam skala logaritmik
# plt.yscale('log')

# Menampilkan grafik
plt.show()