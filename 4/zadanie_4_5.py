import numpy as np

mlen = 8

X = np.random.randint(100, size = (mlen, mlen))
Y = np.random.randint(100, size = (mlen, mlen))
Z = np.random.randint(1, size = (mlen, mlen))

for i in range(mlen):
    for j in range(mlen):
        Z[i][j] = 0

for i in range(mlen):
    for j in range(mlen):
        for k in range(mlen):
            Z[i][j] = Z[i][j] + X[i][k] * Y[k][j]

print(X)
print(Y)
print(Z)
