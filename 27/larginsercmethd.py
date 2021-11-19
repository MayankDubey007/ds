def FindLargeInSearchMethod(arr,low,high):
    if high == low:
        return arr[low]
    if high == low + 1 and arr[low] >= arr[high]:
        return arr[high]
    if high == low + 1 and arr[low] < arr[high]:
        return arr[low]  
    mid = (low + high)//2
    if  arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return arr[mid]
    # p>m>n
    if arr[mid]<arr[mid-1] and arr[mid] > arr[mid+1]:
        return FindLargeInSearchMethod(arr,low,mid-1)
    # p<m<n
    if arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
        return FindLargeInSearchMethod(arr,mid+1,high)
arr = [13,534,5,67,4,77,55,45]
print(FindLargeInSearchMethod(arr,0,len(arr)-1))