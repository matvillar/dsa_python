class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Singly:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_ll(self):
        if self.length <= 0:
            return None
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return False
        elif self.length == 1:
            self.head = None
            self.tail = None
        prev = self.head
        temp = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            return self.append(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return False
        elif self.length == 1:
            self.head = None
            self.tail = None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_node(self, index, value):
        get_index = self.get_node(index)
        if get_index:
            get_index.value = value
            return True
        return False

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        temp = self.get_node(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length:
            return self.pop()
        prev = self.get_node(index - 1)
        temp = self.get_node(index)
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

#     Finish reverse
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp









my_ll = Singly(2)
my_ll.append(4)
my_ll.append(6)

my_ll.prepend(1)
# my_ll.pop_first()
# my_ll.pop_first()
# my_ll.pop()
my_ll.set_node(2, 5)
my_ll.insert(2, 7)
# my_ll.remove(1)
# print("index 3:", my_ll.get_node(3))
my_ll.reverse()
my_ll.print_ll()
