heapify(arr,i,n):
    root = i
    l = 2*i+1
    r = 2*i+2
    if r<n and arr[l]>arr[root]:
        root = l
    if l<n and arr[r]>arr[root]:
        root = r
    if root != i:
        arr[root],arrp[i] = arr[i],arr[]
heapsort(arr):
    n = len(arr)
    for i in range(n//2,-1,-1):
        heapify(arr,i,n)
    for i in range(n-1,-1,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,0,i)
arr = [4,6,87,3,783,45,78,24,8,35,7]