f = lambda x: 5*x**2 - 10
x0, x1 = 1, 2

formula = lambda a, b: (a*f(b)  - b*f(a)) / (5*(b)**2 - 5 * (a)**2)

x2 = formula(x0, x1)
fx0, fx1, fx2 = f(x0), f(x1), f(x2)

print("n", "xn-1", "xn+1", "f(xn+1)", sep="\t\t")

for i in range(50):
    print(i, x0, x1, x2, fx2, sep="\t\t")
    if fx2 * fx0 > 0:
        x0 = x2
        fx0 = fx2
    elif fx2 * fx1 > 0:
        x1 = x2
        fx1 = fx2
    else:
        print("Root Found!")
        break
    x2 = formula(x0, x1)
    fx2 = f(x2)