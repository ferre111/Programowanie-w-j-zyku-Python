import numpy as npmlen = 5X1 = np.random.randint(100, size = (mlen, mlen))def cofactor(X, i, j):    m_tempp = np.delete(X, i, 0)    m_temp = np.delete(m_tempp, j, 1)    return m_tempdef determinant(X):    if len(X) == 2:        value = X[0][0] * X[1][1] - X[1][0] * X[0][1]        return value    Sum = 0    for current_column in range(len(X)):        sign = (-1) ** (current_column)        sub_det = determinant(cofactor(X, 0, current_column))        Sum += (sign * X[0][current_column] * sub_det)    return Sumprint(determinant(X1))print(X1)