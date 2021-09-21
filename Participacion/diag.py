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


def diagArAb(matriz, tama):
    a = np.zeros((tama, tama))
    for f in range(tama):
        for c in range(tama):
            if f == c:
                a[f][c] = matriz[f][c]
    return a


def diagAbAr(matriz, tam):
    a = np.zeros((tam, tam))
    for f in range(tam):
        for c in range(tam - 1, -1, -1):
            if (f + c) == (tam - 1):
                a[f][c] = matriz[f][c]
    return a


print(AB)
print("\n")
print(diagAbAr(AB, 3))
print(diagArAb(AB, 3))
