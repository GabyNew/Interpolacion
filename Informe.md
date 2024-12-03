<h1>Interpolacion</h1>

Estimación de Temperaturas en un Invernadero mediante Interpolación
<h2>se aborda la problemática de estimar temperaturas faltantes en una cuadrícula de sensores de un invernadero. Algunos sensores no están operativos, 
  y se requiere estimar los datos ausentes para mantener un monitoreo uniforme. 
  Utilizamos un método de interpolación lineal para completar el mapa térmico a partir de las lecturas conocidas.
</h2>

<p>Planteamiento del Problema
# Configuración: Una red de sensores distribuidos en una cuadrícula de 
5×5

Sensores con datos disponibles:

<lu>(1,1): 20.5 °C </lu>

<lu>(1,5): 22.3 °C </lu>

<lu>(5,1): 19.8 °C </lu>

<lu>(5,5): 21.7 °C </lu>

<lu>(3,3): 21.0 °C </lu>
Objetivo: Estimar las temperaturas en las posiciones restantes de la cuadrícula para obtener un mapa térmico completo.</p>
<h1>PARA OCTAVE</h1>

% Coordenadas de los sensores con datos conocidos (x, y) y sus temperaturas (z)

x = [1, 1, 5, 5, 3];  % Coordenadas X de los sensores

y = [1, 5, 1, 5, 3];  % Coordenadas Y de los sensores

z = [20.5, 22.3, 19.8, 21.7, 21.0];  % Temperaturas conocidas


% Crear la cuadrícula completa de 5x5

[xq, yq] = meshgrid(1:1:5, 1:1:5);  % Cuadrícula de destino

% Interpolación lineal

zq = griddata(x, y, z, xq, yq, 'linear');

% Visualización

figure;

surf(xq, yq, zq);  % Superficie interpolada

hold on;

plot3(x, y, z, 'ko', 'MarkerFaceColor', 'k');  % Puntos conocidos

title('Interpolación de temperatura');

xlabel('Posición X');

ylabel('Posición Y');

zlabel('Temperatura (°C)');

colorbar;

view(2); % Vista 2D

<H1>PARA PYTHON </H1>

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

