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

    def get_nodes_list(self):

        current = self.head
        nodes_lst = list()
        while current:
            nodes_lst.append(current)
            current = current.next

        return nodes_lst


    def delete_node(self, node):

        if node is None:
            return None

        next = node.next
        node.data = next.data
        node.next = next.next



l = LinkedList()
l.insert_node(10)
l.insert_node(20)
l.insert_node(30)
l.insert_node(40)
l.display_nodes()
print()
print(l.get_nodes_list()[2])

l.delete_node(l.get_nodes_list()[2])
l.display_nodes()

