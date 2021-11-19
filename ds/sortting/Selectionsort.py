# arr = [,136,1,356,1,35,6,346,45,6,56,46,7,56,24,46,4,57,786,1,6,54,6,7,5,36]
arr = [5,9,8,7,6,1,2,3,4]
print(arr) 
n = len(arr)
for i in range(n):
    min = i
    for j in range(i+1,n):
        if arr[min]>arr[j]:
            arr[min],arr[j] = arr[j],arr[min]
print(arr)

# print(arr) 
# n = len(arr)
# print(n) 
# for i in range(n):
#     min = i
#     print(arr[min])
#     for j in range(i+1,n):
#         if arr[min]>arr[j]:
#             arr[min],arr[j] = arr[j],arr[min]
#     if i<n-1:
#         print(f"selection step {i+1}{arr}")
