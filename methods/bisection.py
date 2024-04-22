
from math import e, sin

f = lambda x: x ** 3 + 4 * x ** 2 - 10

x0 = 1
x1 = 2
x2 = (x0 + x1) / 2

fx0, fx1, fx2  = f(x0), f(x1), f(x2)

print("n", "x(n-1)", "x(n)", "x(n+1)", "f(xn+1)", "Diff", sep="\t\t")
print("-"*100)


diff = 0
for i in range(1, 11):
    print(i, x0, x1, x2, fx2,  diff, sep='\t')
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
    x2 = xTemp
    fx2 = f(x2)