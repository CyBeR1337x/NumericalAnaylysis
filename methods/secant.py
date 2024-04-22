f = lambda x: 5*x**2 - 10
x0, x1 = 1, 2

formula = lambda a, b: (a*f(b)  - b*f(a)) / (5*(b)**2 - 5 * (a)**2)

print("n", "xn", sep="\t\t")
print("-"*60)
print(1, 1, sep="\t\t")
print(2, 2, sep="\t\t")

for i in range(3, 12):
    res = formula(x0, x1)
    print(i, res, sep="\t\t")
    x0 = x1
    x1 = res
    if x0 == x1:
        break

print("#"*60)

#table 2
x0, x1 = 1, 2
print("n", "xn-1", "xn", "xn+1", sep="\t\t")
print("-"*60)
for i in range(1, 12):
    res = formula(x0, x1)
    print(i, x0, x1, res, sep="\t\t")
    x0 = x1
    x1 = res
    if x0 == x1:
        break
