import math
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DLL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            new_node.next = temp
            temp.prev = new_node
            self.head = new_node
            self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            return self.pop()
        else:
            temp = self.head
            self.head = temp.next
            self.head.prev = None
            temp.next = None
            self.length -= 1
        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return False
        else:
            if index >= math.ceil(self.length / 2):
                temp = self.tail
                for _ in range(self.length, index, -1):
                    temp = temp.prev
            else:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
        return temp

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return False
        else:
            temp = self.get(index)
            temp.value = value
        return True


dll = DLL(7)
dll.append(9)
dll.append(6)


dll.prepend(1)

dll.set_value(0, 3)


dll.print_list()
