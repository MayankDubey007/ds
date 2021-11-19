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

    def peek(self):
        if self.arr == []:
            return None
        else:
            s = self.arr.copy()
            return s.pop()

    def length(self):
        return len(self.arr)

    def isEmpty(self):
        if self.arr == []:
            return True
        else:
            return False

    def isFull():
        pass


st = stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
# st.peek()
print("******")
print(st.length())
print(st.peek())

# st.size()
print(st.arr)
st.pop()
print(st.arr)
print("******")
print(st.arr)
st.pop()
print(st.arr)
st.pop()
print(st.arr)
st.pop()
print(st.arr)
st.pop()
print(st.arr)
st.pop()
print(st.arr)
