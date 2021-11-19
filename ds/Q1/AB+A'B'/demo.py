def add(x,y):
    print("............ADDTION START...............")
    result = [[0,0,0],
              [0,0,0],
              [0,0,0]]
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[i][j] + y[i][j]
    
    for O in result:
        print(O)
    print("............ADDTION DONE...............")
def multiply(x1,y1):
    print("............Multiplication Start...............")
    result = [[0,0,0],[0,0,0],[0,0,0]]
    for a in range(len(x1)):
        for b in range(len(x1[0])):
            for c in range(len(x1)):
                result[a][b] += x1[a][c] * y1[c][b]
    for m in result:
        print(m)
    print("............Multiplication DONE...............")
b = [[1,2,3],
     [4,5,6],
     [7,8,9]]

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
add(a,b)
multiply(a,b)
    