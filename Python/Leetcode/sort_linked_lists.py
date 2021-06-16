class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_node(self, data):

        if not data:
            return

        node = Node(data)

        if self.head is None:
            node.next = self.head
            self.head = node
            return

        current = self.head

        if current.data > node.data:
            node.next = current
            self.head = node
            return

        while current.next:
            if current.next.data > data:
                break
            current = current.next

        node.next = current.next
        current.next = node


    def display_nodes(self):

        current = self.head

        while current:
            print(current.data, end="->")
            current = current.next



l = LinkedList()
l.insert_node(30)
l.insert_node(10)
l.insert_node(15)
l.insert_node(40)
l.insert_node(35)
l.display_nodes()

