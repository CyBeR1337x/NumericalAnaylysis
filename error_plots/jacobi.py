import numpy as np
import matplotlib.pyplot as plt

A = np.array([[10, 2, 3, 1], 
              [2, 20, 3, 7],
              [3, 5, 30, 7],
              [-5, -6, -2, -30]])

B = np.array([[12], [13], [14], [17]])
x0 = np.array([[0], [0], [0], [0]]) #inital Guess

L = np.tril(A, -1)  #  Lower triangular matrix

U = np.triu(A, 1) #  Upper triangular matrix

D = np.diagflat(np.diag(A))

D_inv = np.linalg.inv(D)
R = A - D

x1 = []
x2 = [] 
x3 = []
x4 = []

for i in range(50):
    print(i+1, np.transpose(x0))
    x1.append(x0[0, 0])
    x2.append(x0[1, 0])
    x3.append(x0[2, 0])
    x4.append(x0[3, 0])
    x0 = np.dot(D_inv, (B - (np.dot(R, x0))))

y = range(len(x1))

plt.plot(y, x1)
plt.plot(y, x2)
plt.plot(y, x3)
plt.plot(y, x4)

plt.legend(['x1','x2','x3','x4'])
plt.show()
