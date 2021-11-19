class stk:
    def __init__(self):
        self.stack = []
    def push(self,value):
        self.stack.append(value)
        print("push > ",value)
    def pop(self):
        print("poped > ",self.stack.pop())
    def prnt(self):
        for i in len(self.stack):
            print("[",i,end=",")
            print("]")
s = stk()
s.push("a")
s.push("b")
s.push("c") 
s.push("d") 
s.push("e") 
s.pop()
s.pop()
s.pop()