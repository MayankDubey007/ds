def multiply(X, Y):
    Mresult = [[0, 0],
               [0, 0]]
    for i in range(len(Y)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                Mresult[i][j] += X[i][k] * Y[k][j]

    for O in Mresult:
        print(O)
    return Mresult


def main():
    m1 = [[1, 2],
          [3, 4]]

    m2 = [[5, 6],
          [7, 8]]

    multiply(m1, m2)

if(__name__ == "__main__"):
    main()
    
# # iterate through rows of X
# for i in range(len(X)):
#    # iterate through columns of Y
#    for j in range(len(Y[0])):
#        # iterate through rows of Y
#        for k in range(len(Y)):
#            result[i][j] += X[i][k] * Y[k][j]

# for r in result:
#    print(r)
