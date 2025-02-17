import numpy as np

arr = np.arange(10, 50)
arr = arr.reshape(4, 10)
print(arr.shape)

segunda_fila = arr[1]
print(segunda_fila)
cuarta_fila = arr[3]
print(cuarta_fila)

mean = np.mean(arr, axis=0)
print(mean)
