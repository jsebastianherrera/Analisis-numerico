# Implementación del método de Punto Fijo para encontrar las raices de una función dada

from matplotlib import pyplot
import numpy
import math


def G1(x):
    return lambda x: x ** 3 - 2 * x - 5


def puntoFijo1(a, b):

    x = (a + b) / 2
    tol = 10e-8
    it = 0
    errorX = []
    errorY = []

    while abs(G1(x) - x) > tol:
        if it > 0:
            errorX.append(abs(G1(x) - x))
        it = it + 1
        x = G1(x)
        if it > 1:
            errorY.append(abs(G1(x) - x))

    print(
        "La raiz que se encuentra en el intervalo ",
        a,
        ", ",
        b,
        " con la funcion g(x) = e ^ x / PI es aproximadamente: ",
        x,
    )
    print("El numero de iteraciones que se obtuvieron: ", it)

    cX = numpy.linspace(errorX[0], errorX[len(errorX) - 1], 50)
    cY = numpy.linspace(errorY[0], errorY[len(errorY) - 1], 50)
    pyplot.plot(cX, cY)
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Metodo de Punto Fijo: \n Errores en X vs. Errores en Y")
    pyplot.grid()
    pyplot.show()


# ------------------------MAIN------------------------------------------

if __name__ == "__main__":
    puntoFijo1(0, math.pi)
