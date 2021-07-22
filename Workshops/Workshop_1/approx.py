import numpy as np
from numpy.lib import polynomial
import sympy as sym
import math
x = sym.Symbol('x')
fx = sym.euler(x)
x0 = 3
n = 3
# Process
k = 0
polynomial = 0
while not (k > n):
    derivate = fx.diff(x, k)
    derivatex0 = derivate.subs(x, x0)
    divider = math.factorial(k)
    kterm = (derivatex0/divider)*(x-x0)**k
    polynomial += kterm
    k = k+1
print(polynomial)
