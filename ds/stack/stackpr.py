def push(list,item):
    list.append(item)
def pop(list):
    if not list:
        print("NOW this list is empty")
    else:
        list.pop()
ls= []
#   PUSH
print("PUSH METHOD")
print(ls)
push(ls,1)
print(ls)
push(ls,2)
print(ls)
push(ls,3)
print(ls)
push(ls,4)
print(ls)
push(ls,5)
print(ls)
#   POP
print("POP METHOD")
print(ls)
pop(ls)
print(ls)
pop(ls)
print(ls)
pop(ls)
print(ls)
pop(ls)
print(ls)
pop(ls)
print(ls)
pop(ls)