class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = node
        node.prev = p

    def traverse(self):
        if self.head is None:
            print("No nodes in the list")
            return
        else:
            p = self.head
            while p is not None:
                print("Data: ",p.data)
                p = p.next

    def delete_at_beginning(self):
        if self.head is None:
            print("No nodes in the list")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self):
        if self.head is None:
            print("No nodes in the list")
            return
        if self.head.next is None:
            self.head = None
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.prev.next = None

dll = DoubleLinkedList()
dll.append(10)

dll.append(20)
dll.append(30)
dll.append(40)
dll.delete_at_beginning()
dll.delete_at_end()
dll.traverse()



