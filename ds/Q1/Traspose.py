X = [[12, 7],
     [4, 5],
     [3, 8]]

result = [[0, 0, 0],
          [0, 0, 0]]
for r in range(len(X)):
    for c in range(len(X[0])):
        result[c][r] = X[r][c]
for A in result:
    print(A)