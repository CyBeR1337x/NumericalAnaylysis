f = lambda x: 5*x**2 - 10
fd = lambda x: 10*x
sol = lambda x: x - (f(x) / fd(x))

x0 = 1.5
print("n", "xn", sep="\t")
print("-"*30)
for i in range(10):
    print(i, x0, sep="\t")
    x0 = sol(x0)