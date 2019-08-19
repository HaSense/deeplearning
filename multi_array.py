'''

다차원 배열을 이용한 계산법을 숙달하면 
신경망을 효율적으로 구현하는데 도움이 됩니다.

다차원 배열 연습입니다.

'''

import numpy as np

A = np.array([1,2,3,4])
print(A)
print(f'배열의 차원수 : {np.ndim(A)}차원')
print(f'배열의 형상 : {A.shape}')
print(A.shape[0])

B = np.array([[1, 2], [3, 4], [5, 6]])
print(B)
print(f'배열의 차원수 : {np.ndim(B)}차원')
print(f'배열의 형상 : {B.shape}')

C = np.array([[1,2], [3,4]])
print(C.shape)
D = np.array([[5,6], [7,8]])
print(D.shape)
print(np.dot(C, D))

E = np.array([[1,2,3], [4,5,6]])
print(E.shape)
F = np.array([[1,2], [3,4],[5,6]])
F.shape
print(np.dot(E,F))


G = np.array([[1,2], [3,4]])
print(G.shape)
print(E.shape)

# print(np.dot(E,G))  #배열의 차원이 서로 맞지않아 에러발생


A = np.array([[1,2], [3,4], [5,6]])
print(A.shape)
B = np.array([7,8])
print(B.shape)
print(np.dot(A,B))

#신경망에서의 행렬 곱
X = np.array([1, 2])
W = np.array([[1,3,5], [2,4,6]])
Y = np.dot(X,W)
print(Y)
 
