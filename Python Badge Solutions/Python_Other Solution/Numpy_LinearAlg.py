import numpy
N = int(input())
A = numpy.array([input().split() for i in range(N)], dtype=float)
det=numpy.linalg.det(A)
print(round(det, 2))
