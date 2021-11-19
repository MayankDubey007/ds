def missNum(arr):
    n = len(arr)
    valuesum = ((n+2)*(n+1))//2
    return valuesum - sum(arr)
    # pass
arr=[1,2,3,5,6]
print(missNum(arr))