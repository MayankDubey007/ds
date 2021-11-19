blank=[]
filled=[11,2,3,5,6,7]
# First Way To Create  pop function Without Error
def pop1(list):
    if len(list)>0:
        list.pop()
    else:
        print("this list is empty")
# ls=[]
# pop1(ls)
# Second Way To Create  pop function Without 
def pop2(list):
    if not list:
        print("empty")
    else:
        list.pop()
print(blank)

pop1(blank)

print(filled)

pop1(filled)

print(filled)