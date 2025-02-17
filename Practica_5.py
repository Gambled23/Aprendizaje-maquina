import numpy as np
# crear matriz de 5x5 con elementos aleatorios entre 0 y 1
A = np.random.rand(5,5)
B = np.random.rand(5,3)

x = np.zeros((5, 50))
x[:, 0] = np.random.rand(5)
