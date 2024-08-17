import numpy as np
A = np.array([input().split() for _ in range(int(input().split()[0]))], int)
print(np.mean(A, axis=1), np.var(A, axis=0), round(np.std(A), 11), sep='\n')


