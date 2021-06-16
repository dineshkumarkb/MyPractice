class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_head(self, data):

        if not data:
            return

        node = Node(data)
        node.next = self.head
        self.head = node

    def display_nodes(self):

        current = self.head

        while current:
            print(current.data, end="->")
            current = current.next

    def delete_nth_node(self, n):

        p1 = self.head
        p2 = self.head


        for i in range(n):
            p1 = p1.next

        while p1.next:
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next





l = LinkedList()
l.insert_at_head(10)
l.insert_at_head(20)
l.insert_at_head(30)
l.insert_at_head(40)

l.display_nodes()

l.delete_nth_node(2)

print()
l.display_nodes()