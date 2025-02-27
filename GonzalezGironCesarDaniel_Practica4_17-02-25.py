# Objetivo: Crear un programa que simule un sistema dinámico
import numpy as np # Importar librería numpy
# crear matriz de 5x5 con elementos aleatorios entre 0 y 1
A = np.random.rand(5,5)
B = np.random.rand(5,3)

x = np.zeros((5, 50))
x[:, 0] = np.random.rand(5)

u = np.random.rand(3, 50) # Control
for t in range (1, 50): # 50 pasos de tiempo
    x[:, t] = np.dot(A, x[:, t-1]) + np.dot(B, u[:, t-1])

print(f'Estados finales: {x[:, -1]}')