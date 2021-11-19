class stack:
    def __init__(self):
        self.arr = []
    def push(self, data):
        self.arr.append(data)
    def pop(self):
        if not self.isEmpty():
            self.arr.pop()
        else:
            print("Stack is Empty")
    def size(self):
        return len(self.arr)

    def isEmpty(self):
        if self.arr == []:
            return True
        else:
            return False



st = stack()
print(st.arr)

st.push("cd")
st.push("cd")
st.push("cd")
st.push("cd")
st.push("cd")
print("[0]-> 5 insert")

print(st.arr)
st.pop()
st.pop()
print("[1]-> 2 pop")

print(st.arr)
st.push("cd")
st.push("cd")
st.push("cd")
print("[2]-> 3 insert")
print(st.arr)

st.pop()
print("[3]-> 1 pop")
print(st.arr)

st.push("cd")
st.push("cd")
print("[4]-> 2 insert")
print(st.arr)

print("[4]-> Total No Of CDs")
print(st.size())
