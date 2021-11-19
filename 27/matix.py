# class matrix:
#     def add(x,y):
#         result =[[0,0],
#                  [0,0]]
#         for i in range(len(x)):
#             for j in range(len(y[0])):
#                 result[i][j] = x[i][j] + y[i][j]
                
#         for o in result:
#             print(o)
#         return result
# m = matrix()
 
# a = [[1,3],
#     [3,4]]
# b = [[4,3],
#     [2,1]]
# m.add(a,b)
def add(x,y):
    result =[[0,0],
             [0,0]]
    for i in range(len(x)):
        for j in range(len(y[0])):
            result[i][j] = x[i][j] + y[i][j]
            
    for o in result:
        print(o)
    return result
def mltpy(x,y):
    result =[[0,0],
             [0,0]]
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(x)):
                result[i][j] += x[i][k] * y[k][j]
    for A in result:
        print(A)
    return result
def transpose(x):
    result =[[0,0],
             [0,0]]
    for i in range(len(x)):
        for j in range(len(x[0])):
            result[i][j] = x[j][i]
    for k in result:
        print(k)
    return result
a = [[1,3],
    [3,4]]
b = [[4,3],
    [2,1]]
# add(a,b)
mltpy(a,b)
transpose(b)