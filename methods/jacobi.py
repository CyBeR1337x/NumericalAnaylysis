import numpy as np

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

for i in range(50):
    print(i+1, np.transpose(x0))
    x0 = np.dot(D_inv, (B - (np.dot(R, x0))))