class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Sl:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        if self.length <= 0:
            return None
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length <= 0:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            prev = self.head
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
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        index_node = self.get(index)
        if index_node:
            index_node.value = value
            return True
        return False

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        temp = self.get(index)
        prev = self.get(index - 1)
        prev.next = new_node
        new_node.next = temp
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        prev = self.get(index - 1)
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after





ll = Sl(1)
ll.append(2)
ll.append(3)
ll.append(4)

# ll.insert(0, 7)
# ll.insert(1, 8)



ll.print_list()

ll.reverse()
ll.print_list()