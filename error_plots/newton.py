from math import e, sin, cos
from matplotlib.pyplot import show, plot

f = lambda x: e ** x * sin(x**2) - 10
fd = lambda x: e ** x * (sin(x ** 2) + 2*x*cos(x ** 2))
sol = lambda x: x - (f(x) / fd(x))

x0 = (7 + 8) / 2
print("n", "xn", sep="\t")
diffPlot = []
print("-"*30)
for i in range(10):
    print(i, x0, sep="\t")
    xt = sol(x0)
    diffPlot.append(abs(xt - x0))
    x0 = xt

it = range(len(diffPlot))
plot(it, diffPlot)
show()



