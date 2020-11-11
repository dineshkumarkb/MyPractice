class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_next(self, new_next):
        self.next = new_next

    def get_next(self):
        self.next





class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert_node(self,data):

        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node



l = LinkedList()
l.insert_node(10)
l.insert_node(20)
l.insert_node(30)
l.insert_node(40)
l.insert_node(10)

def find_duplicate():

    node = l.head
    copy_lst = list()
    while node is not None:
        if node.data in copy_lst:
            print(f" Node data: {node.data} ")
            return node.data
        else:
            copy_lst.append(node.data)
        node = node.next


print(find_duplicate())