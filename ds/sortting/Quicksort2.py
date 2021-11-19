def swap(a,b,ls):
    if a!=b:
        temp = ls[a]
        ls[a] = ls[b]
        ls[b] = temp
ls = [12,3,55,64,5,14,4,6,61,24,35,63,5]
print(ls)
def partion(ls,start,end):
    pivot_index = start
    pivot  = ls[pivot_index]
    while start < end:
        while start < len(ls) and ls[start]<=pivot:
            start+=1
        while ls[end] > pivot:
            end-=1
        if start<end:
            swap(start,end,ls)        
    swap(pivot_index,end,ls)
    return end
print(partion(ls,0,len(ls)-1))
print(ls)
