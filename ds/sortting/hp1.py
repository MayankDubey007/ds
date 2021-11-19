heapsort(arr):
    ln = len(arr)
    for i in range(ln//2,-1,-1):
        heapify(arr,ln,i)
    for i in range(ln-1,-1,-1):
        heapify(arr,ln,i)
arr = [1,7,3,89,123,62,56,7,8,5]
heapsort(arr)