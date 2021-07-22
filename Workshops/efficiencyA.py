import numpy as np
import sympy as sym
from sympy.core.sympify import sympify
from sympy.polys.polytools import factor
x, y = sym.symbols('x y')
expre = "x**3-2*x**2+4*x/3-8/27"
cont = 0
try:
    expre = factor(expre)
    cont += 1
    print(sym.sympify(expre).subs(x, 4))
    print(cont)
except:
    print("sad")
