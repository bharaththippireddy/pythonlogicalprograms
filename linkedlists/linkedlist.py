class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = node

    def traverse(self):
        p = self.head
        while p is not None:
            print(p.data)
            p = p.next

    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_in_the_middle(self, pos,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        elif pos == 0:
            node.next = self.head
            self.head = node
        else:
            p = self.head
            for i in range(1, pos):
                p = p.next
            node.next = p.next
            p.next = node

    def remove_from_beginning(self):
        self.head = self.head.next

    def remove_from_end(self):
        current_node = self.head
        previous_node = self.head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None

    def reverse(self):
        next_node = None
        prev_node = None
        while self.head is not None:
            next_node = self.head.next
            self.head.next = prev_node
            prev_node = self.head
            self.head = next_node
        self.head = prev_node

    def has_loop(self):
        slow_ptr, fast_ptr = self.head
        while slow_ptr and fast_ptr is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return True
        return False

list1 = LinkedList()
list1.insert_at_end("TWO")
list1.insert_at_end("THREE")
list1.insert_at_beginning("ONE")
list1.insert_in_the_middle(0, "ZERO")
# list1.remove_from_beginning()
# list1.remove_from_beginning()
# list1.remove_from_end()
list1.traverse()
list1.reverse()
list1.traverse()