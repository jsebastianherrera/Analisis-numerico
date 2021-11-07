import sympy as sy
import matplotlib.pyplot as plt


# Define the variable and the function to approximate
x = sy.Symbol('x')
f = x*sy.exp(3*x)-40

# Factorial function


def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)

def taylor(function, x0, n):
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x, i).subs(x, x0))/(factorial(i))*(x-x0)**i
        i += 1
    return p

val=[0.4,0.01,1.55]
y=sy.simplify(taylor(f, 0, 4))
l=[]
for i in val:
    l.append({'Real':f.subs(x,i),'Aprox':y.subs(x,i),'Error':abs(f.subs(x,i)-y.subs(x,i))})

print('POL TAYLOR:',y   )
for i in l:
    print(i)
print(f.subs(x,0.9))
print(y.subs(x,0.9))
abs(f.subs(x,0.9)-y.subs(x,0.9))