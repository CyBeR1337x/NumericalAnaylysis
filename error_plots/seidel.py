import numpy as np
import matplotlib.pyplot as plt

A = np.array([[10, 1, -1, -1, 1], 
              [3, 17, -1, -1, -1],
              [1, -1, 20, -4, 1],
              [3, -1, 3, 25, -1],
              [4, -1, 1, -4, 18]])

B = np.array([[10], [20], [18], [22], [19]])
x0 = np.array([[1], [1], [1], [0], [0]]) #inital Guess



#method 1 to compute D & R
L = np.tril(A, -1) 
#-1 doesn't include principle diagnol (remove for testing)
# principle diagonal has index 0 above is + 1 and below is -1 
U = np.triu(A, 1)
# D = A - L - U
#R = L + U

#method 2 to compute D

D = np.diagflat(np.diag(A))
print(D)
D_inv = np.linalg.inv(D)
R = A - D
x1 = []
x2 = [] 
x3 = []
x4 = []
x5 = []
for i in range(30):
    print(i+1, np.transpose(x0))
    x1.append(x0[0, 0])
    x2.append(x0[1, 0])
    x3.append(x0[2, 0])
    x4.append(x0[3, 0])
    x5.append(x0[4, 0])
    x0 = np.dot((np.linalg.inv(L + D)), (B - np.dot(U, x0)))

y = range(len(x1))

plt.plot(y, x1)
plt.plot(y, x2)
plt.plot(y, x3)
plt.plot(y, x4)
plt.plot(y, x5)
plt.legend(['x1','x2','x3','x4', 'x5'])
plt.show()
