X = int(input())
Y = int(input())
Z = int(input())

permutation = [[i, j, k] for i in range(X + 1) for j in range(Y + 1) for k in range(Z + 1)]
print(permutation)