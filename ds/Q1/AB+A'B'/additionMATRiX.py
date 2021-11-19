def ADD(X,Y):
    result = [[0,0],
              [0,0]]
    for i in range(len(X)):  
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]

    for r in result:
        print(r)
    return result
    
def main():
    X1 = [[1,3],
        [7 ,9]]
    
    Y1 = [[9,7],
        [3,2]]
    
    
    ADD(X1,Y1)
if (__name__=="__main__"):
    main()
    
