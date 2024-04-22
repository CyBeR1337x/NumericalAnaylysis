import matplotlib.pyplot as plt

f = lambda x: 5*x**2 - 10

formula = lambda a, b: (a*f(b)  - b*f(a)) / (5*(b)**2 - 5 * (a)**2)
diffPlot = []
x0, x1 = 1, 2
res = formula(x0, x1)
diffPlot = []
for i in range(10):
    res = formula(x0, x1)
    x0 = x1
    x1 = res
    if x0 == x1:
        break

    diffPlot.append(formula(x0, x1) - res)

iterations = range(len(diffPlot))
plt.plot(diffPlot, iterations)
plt.show()