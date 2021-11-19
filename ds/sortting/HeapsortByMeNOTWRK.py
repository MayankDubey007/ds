 def heapify(arr, ln, i):
    root = i
    l = 2*i+1 
    r = 2*i+2
    if l<ln and arr[l]>arr[root]:
        root = l
    if r<ln and arr[r]>arr[root]:
        root = r
    if root != i:
        arr[i],arr[root] = arr[root],arr[i]
        heapify(arr,ln,root)
def heapsort(arr):
    ln = len(arr)
    # build heap
    strInX = ln//2
    for i in range(strInX,-1,-1):
        heapify(arr,ln,i)
    # extract element
    for i in range(ln-1,-1,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0) #dif
arr = [4,6,87,3,783,45,78,24,8,35,7]
heapsort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print(f"{arr[i]}",end=" ")