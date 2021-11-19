def mergesort(array):
    if len(array) < 2:
        return array
    
    mid = len(array)//2
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])
    return merge(left,right)



def merge(left,right):
    result = []
    l,r = 0,0
    while l<len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l+=1
        else: 
            result.append(right[r])
            r+=1
        # print(f"l = {l}\nr = {r}")
        if  l == len(left) or r == len(right):
            result.extend(left[l:] or right[r:])
            break
    return result
array = [2,5,6,1,4,3]
print(mergesort(array))
# a = [1,2,3]
# b = [1,2,3]
# print(merge(L,R))
# b.extend(a)
# print(b)