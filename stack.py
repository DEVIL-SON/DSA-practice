class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        if self.height == 0:
            print("Stack is Empty")
        else:
            temp = self.top
            while temp is not None:
                print(temp.value)
                temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -= 1
        return temp.value
        
my_stack = Stack(3)
my_stack.push(1)
my_stack.push(2)
print("stack pop method")
print(my_stack.pop())
print("Stack Printing")
my_stack.print_stack()