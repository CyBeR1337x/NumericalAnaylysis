
from math import e, sin
import matplotlib.pyplot as plt

f = lambda x: e ** x * sin(x ** 2) - 10

x0 = 7
x1 = 8
x2 = (x0 + x1) / 2

fx0, fx1, fx2  = f(x0), f(x1), f(x2)

diff = 0
diffPlot = []

for i in range(10):
    if fx2 * fx0 > 0:
        x0 = x2
        fx0 = fx2
    elif fx2 * fx1 > 0:
        x1 = x2
        fx1 = fx2
    else:
        break

    xTemp = (x0 + x1) / 2
    diff = abs(xTemp - x2)
    diffPlot.append(diff)
    x2 = xTemp
    fx2 = f(x2)

iterations = range(len(diffPlot))
plt.plot(diffPlot, iterations)
plt.show()