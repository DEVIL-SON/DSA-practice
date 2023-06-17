class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def empty_the_list(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_linked_list(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.value)
                n = n.next

    def add_element_from_behind(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            # self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.head is None: return None
        pre = temp = self.head
        while temp.next != None: pre=temp; temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length = self.length -1 
        if self.length == 0:
            self.head = self.tail = None
        return temp.value


    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node 

    def pop_first(self):
        if self.length == 0 or self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value


    def sets(self, index, value):
        if index < 0 or index >= self.length: return None
        temp = self.head
        for _ in range(index): temp = temp.next
        temp.value = value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True    

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_Linked = List(4)
my_Linked.empty_the_list()
my_Linked.add_element_from_behind(10)
my_Linked.add_element_from_behind(20)
my_Linked.add_element_from_behind(30)
my_Linked.add_element_from_behind(40)
my_Linked.pop()
my_Linked.pop()
my_Linked.pop()
my_Linked.prepend(50)
# my_Linked.pop_first()
# print(my_Linked.pop_first())
# print(my_Linked.get(1))
my_Linked.sets(1, 30)
my_Linked.print_linked_list()
