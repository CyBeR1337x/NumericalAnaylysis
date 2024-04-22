import numpy as np

A = np.array([[10, 1, -1, -1, 1], 
              [3, 17, -1, -1, -1],
              [1, -1, 20, -4, 1],
              [3, -1, 3, 25, -1],
              [4, -1, 1, -4, 18]])

B = np.array([[10], [20], [18], [22], [19]])
x0 = np.array([[1], [1], [1], [0], [0]]) #inital Guess



L = np.tril(A, -1) 
U = np.triu(A, 1)
D = np.diagflat(np.diag(A))

for i in range(30):
    print(i+1, np.transpose(x0))
    x0 = np.dot((np.linalg.inv(L + D)), (B - np.dot(U, x0)))


