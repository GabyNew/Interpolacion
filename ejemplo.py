import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Coordenadas de los sensores con datos conocidos (x, y) y sus temperaturas (z)
points = np.array([
    (1, 1),  # Coordenadas del sensor 1
    (1, 5),  # Coordenadas del sensor 2
    (5, 1),  # Coordenadas del sensor 3
    (5, 5),  # Coordenadas del sensor 4
    (3, 3)   # Coordenadas del sensor 5
])

values = np.array([20.5, 22.3, 19.8, 21.7, 21.0])  # Temperaturas correspondientes

# Coordenadas de la cuadrícula completa (5x5) donde se necesitan estimaciones
grid_x, grid_y = np.mgrid[1:6, 1:6]

# Interpolación bilineal
grid_z = griddata(points, values, (grid_x, grid_y), method='linear')

# Visualización de resultados
plt.figure(figsize=(8, 6))
plt.imshow(grid_z, extent=(1, 5, 1, 5), origin='lower', cmap='coolwarm', alpha=0.8)
plt.colorbar(label='Temperatura (°C)')
plt.scatter(points[:, 0], points[:, 1], color='black', label='Sensores conocidos')
plt.title("Interpolación de temperatura en la cuadrícula")
plt.xlabel("Posición X")
plt.ylabel("Posición Y")
plt.legend()
plt.show()

grid_z
