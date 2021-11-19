def enqueue(list,item):
    list.append(item)

def dequeue(list):
    if not list:
        print("now this queue is  empty ")
    else:
            list.pop(0)

ls = []
print(ls)
print("ENQUEUE OPREATION")
#          ENQUEUE OPREATION 
enqueue(ls,1)
print(ls)
enqueue(ls,2)
print(ls)
enqueue(ls,3)
print(ls)
enqueue(ls,4)
print(ls)
enqueue(ls,5)
print(ls)
#          DEQUEUE OPREATION 
print("DEQUEUE OPREATION")
dequeue(ls)
print(ls)
dequeue(ls)
print(ls)
dequeue(ls)
print(ls)
dequeue(ls)
print(ls)
dequeue(ls)
print(ls)
dequeue(ls)