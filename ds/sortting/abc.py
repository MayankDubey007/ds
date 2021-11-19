ls = [8, 27, 35, 27, 44, 67, 3, 986, 21, 65, 1, 5, 17]
n = len(ls)
for i in range(0, n):
    for j in range(0, n-1):
        if ls[j] > ls[j+1]:
            # ls[j],ls[j+1] = ls[j+1],ls[j]
            temp = ls[j]
            ls[j] = ls[j+1]
            ls[j+1] = temp
for e in range(n):
    print(ls[e], end=" ")
