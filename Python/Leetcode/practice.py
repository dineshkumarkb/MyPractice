class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.current = None

    def insert_node(self, data):

        node = Node(data)

        if self.head is None:
            node.next = self.head
            self.head = node
            self.current = self.head
        else:
            self.current.next = node
            self.current = self.current.next

    def display_nodes(self):

        current = self.head

        while current:
            print(current.data, end="->")
            current = current.next


l = LinkedList()
l.insert_node(10)
l.insert_node(20)
l.insert_node(30)
l.insert_node(40)
l.display_nodes()

