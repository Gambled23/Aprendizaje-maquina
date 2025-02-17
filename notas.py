import numpy as np

arr = np.array(10)
arr2 = np.array([1, 2, 3, 4, 5])
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr.ndim, arr.shape)
print(arr2.ndim, arr2.shape)
print(arr3.ndim, arr3.shape)
print(arr4.ndim, arr4.shape)

# Crear matriz de nxm con 0 elementos
arr5 = np.zeros((3, 2))
print(arr5)

arr6 = np.arange(10, 50)
print(arr6)
arr6 = arr6.reshape(4, 10)
print(arr6)