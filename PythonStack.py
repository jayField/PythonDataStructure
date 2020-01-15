class Stack:

    def __init__(self):
        self.stack_items = []

    # delete item
    def pop(self):
        item_length = len(self.stack_items)

        if item_length < 1:
            print("Stack is empty")
            return False

        result = self.stack_items[-1]
        del self.stack_items[-1]
        return result

    # add item
    def push(self, x):
        self.stack_items.append(x)

    # check Stack
    def isEmpty(self):
        return not self.stack_items

    def printStack(self):
        print(self.stack_items)


st = Stack()
st.printStack()
print(st.isEmpty())
st.push(1)
st.push(3)
st.push(5)
st.push(7)
st.push(9)
st.printStack()
print(st.isEmpty())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.isEmpty())