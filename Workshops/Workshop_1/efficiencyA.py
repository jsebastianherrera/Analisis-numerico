import numpy as np
import sympy as sym
from sympy.polys.polytools import factor
x = sym.symbols('x')
expre = "x**3-2*x**2+4*x/3-8/27"
cont = 0
try:
    expre = factor(expre)
    cont += 1
    #print(sym.sympify(expre).subs(x, 4))
    print(expre)
except:
    print("sad")
