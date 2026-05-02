import numpy as np

matrix1 = np.array([
    [2, -1, 1],
    [1, 2, 3],
    [-2, 1, 2]
])

matrix2 = np.array([
    [0, 2, -3],
    [1, 1, 0],
    [2, -1, 1]
])

# Use the @ operator for matrix multiplication
result = matrix1 @ matrix2

print(result)