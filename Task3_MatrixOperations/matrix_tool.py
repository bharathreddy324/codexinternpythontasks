import numpy as np

def display(matrix):
    for row in matrix:
        print(row)

print("Enter size of matrix A (rows and columns):")
r, c = map(int, input().split())
print("Enter elements of matrix A:")
A = np.array([list(map(int, input().split())) for _ in range(r)])

print("Enter size of matrix B (rows and columns):")
r2, c2 = map(int, input().split())
print("Enter elements of matrix B:")
B = np.array([list(map(int, input().split())) for _ in range(r2)])

print("\nMatrix A:")
display(A)
print("Matrix B:")
display(B)

print("\nAddition:")
if A.shape == B.shape:
    display(A + B)
else:
    print("Not possible")

print("\nSubtraction:")
if A.shape == B.shape:
    display(A - B)
else:
    print("Not possible")

print("\nMultiplication:")
if A.shape[1] == B.shape[0]:
    display(np.dot(A, B))
else:
    print("Not possible")

print("\nTranspose of A:")
display(A.T)

if A.shape[0] == A.shape[1]:
    print("\nDeterminant of A:", np.linalg.det(A))
else:
    print("\nDeterminant not possible for non-square matrix")
