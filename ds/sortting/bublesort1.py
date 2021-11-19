
arr = [9,8,7,6,5,4,3,2,1]
n = len(arr)
print(arr)
for i in range(n):
    for j in range(n-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)

arr = [9,8,7,6,5,4,3,2,1]
n = len(arr)
print(arr)
for i in range(n):
    for j in range(n-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
    if i<n-1:
        print(f"Pass {i+1}    {arr}")
    
print(arr)