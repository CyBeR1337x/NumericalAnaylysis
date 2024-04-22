import numpy as np
import matplotlib.pyplot as plt
A = np.array([[-4, 1], 
              [-1, 1],
              ])

B = np.array([[7], [7]])
x0 = np.array([[1], [1]]) #inital Guess

x1, x2 = [], []
L = np.tril(A, -1) 

U = np.triu(A, 1)
D = np.diagflat(np.diag(A))

w = 0.9 # omega

for i in range(20):
    print(i+1, np.transpose(x0))
    x1.append(x0[0, 0])
    x2.append(x0[1, 0])
    x0 = np.dot(np.linalg.inv(((D / w) + L)), B + (np.dot((D / w) - U - D, x0)))

y = range(len(x1))

plt.plot(y, x1)
plt.plot(y, x2)
plt.legend(['x1', 'x2'])
plt.show()
