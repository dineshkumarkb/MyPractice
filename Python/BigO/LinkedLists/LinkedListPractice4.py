class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert_node(self, data):

        if data is None:
            return

        node = Node(data)
        node.next = self.head
        self.head = node

    def display_lst(self):

        if not self.head:
            return "Empty list"

        ll_data = list()

        current = self.head
        while current:
            ll_data.append(current.data)
            current = current.next

        print(ll_data)

    def partition_lst(self, part_value):

        # Initialize two pointers at head and tail
        current = self.head
        end = self.head

        while current:
            next_node = current.next
            if current.data < part_value:
                current.next = self.head
                self.head = current
            else:
                end.next = current
                end = current

            current = next_node

        end.next = None



l = LinkedList()
l.insert_node(1)
l.insert_node(2)
l.insert_node(8)
l.insert_node(2)
l.insert_node(10)
l.insert_node(5)
l.display_lst()
l.partition_lst(5)
l.display_lst()



