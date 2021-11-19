def reverse(string):
    stk = stack()
    ls = []
    newstr = ""
    for i in string:
        stk.push(i)
    ls = stk.getStack()
    for j in range(len(ls)):
        newstr += ls.pop()
    print(newstr)
