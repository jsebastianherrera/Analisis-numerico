import numpy as np

A = np.array(
    [
        [2, 1, 1],
        [-1, -1, 11],
        [0.5, 0, 1],
    ]
)
B = np.array([[3], [6], [-1]])
AB = np.concatenate((A, B), axis=1)
tamano = np.shape(AB)
# Row
n = tamano[0]
# Column
m = tamano[1]
# Init cont
contador = 1
for i in range(0, n - 1):
    columna = abs(AB[i:, i])
    max = np.argmax(columna)
    if max != 0:
        # intercambia filas
        temporal = np.copy(AB[i, :])
        AB[i, :] = AB[max + i, :]
        AB[max + i, :] = temporal
        contador += 1

for i in range(0, n - 1):
    pivote = AB[i, i]
    adelante = i + 1
    for k in range(adelante, n, 1):
        factor = AB[k, i] / pivote
        AB[k, :] = AB[k, :] - AB[i, :] * factor
        contador += 1
print(factor)
ultfila = n - 1
ultcolumna = m - 1
for i in range(ultfila, 0 - 1, -1):
    pivote = AB[i, i]
    atras = i - 1
    for k in range(atras, 0 - 1, -1):
        factor = AB[k, i] / pivote
        AB[k, :] = AB[k, :] - AB[i, :] * factor
        contador += 1
    # diagonal a unos
    AB[i, :] = AB[i, :] / AB[i, i]

X = np.copy(AB[:, ultcolumna])
X = np.transpose([X])

print(X)
