def trns(X):
    result = [[0, 0],
              [0, 0]]
    for r in range(len(X)):
        for c in range(len(X[0])):
            result[c][r] = X[r][c]
    return result

def main():
    X = [[12, 7],
         [4, 5],
         [3, 8]]
    # print
    trns(X)

if (__name__=="__main__"):
    main()