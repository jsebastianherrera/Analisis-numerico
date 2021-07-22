import os
import sys
# Create an sqrt function
os.system("clear")
i = int(len(sys.argv))
if (i-1 == 3 and float(sys.argv[1]) >= 0):
    n = float(sys.argv[1])
    e = sys.argv[2]
    x = float(sys.argv[3])
else:
    print("Check parameters")
    exit(0)


def calculate(x, n):
    try:
        return (1/2)*(x+(n/x))
    except:
        print("Error: Float division by zero")
        exit(0)


y = calculate(x, n)
while abs(x-y) > float(e):
    print("Y:", y)
    x = y
    y = calculate(x, n)
