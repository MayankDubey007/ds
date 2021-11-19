open = ["[","{","("]
close = ["]","}",")"]
mystr = "{[]{()}}"
def check(mystr):
    stack = []
    top = len(stack)-1
    for i in mystr: #scan element in given string
        if i in open: #agar scaned element(i)  open me ho toh
            stack.append(i)#stack me push kardo (element ko stack ke last me append kardo)
        elif i in close:#agar scaned element(i)  close me ho toh
            pos = close.index(i)#toh us element ki closelist me index ko pos me dalna hai (beacause if open[pos] = { then close[pos]=})
            if ((len(stack)>0)and(open[pos]==stack[top])):#CONDITION = ager openlist[pos] ka element stack ka top element hai toh (agar  closelist[i] = } toh openlist[i] = {)
                stack.pop()#(main condition ->stack se top element ko pop kardo)
            else:
                return "unbalanced"    #nahi toh return = unbalanced
    if len(stack)==0: #agar stack ki length  == 0 ho toh 
        return "balanced" 
    else:# nahi toh
        return "unbalanced"
string = "{[]{()}}"
print(string,"-", check(string))