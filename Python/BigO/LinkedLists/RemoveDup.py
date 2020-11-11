class Node(object):
    """
    This Node class is used to create nodes for a linked list
    It has the following methods
    1. get next
    2. set next

    """

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert_node(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display_nodes(self):

        current = self.head

        elements = list()

        while current is not None:
            elements.append(current.data)
            current = current.next

        return elements

    def remove_duplicates(self):
        # Initialize the current pointer to head
        current = self.head
        prev = None

        # Initialize a copy list to store duplicates
        copy_lst = list()

        # Check for end of linkedlist
        while current is not None:
            print(f" Current data: {current.data}")
            if current.data in copy_lst:
                print(f" Removing duplicate: {current.data}")
                prev.next = current.next
            else:
                copy_lst.append(current.data)
                prev = current
            current = current.next

    def remove_duplicates_wo_addl_ds(self):

        current = self.head
        prev = None

        while current is not None:
            runner = current
            while runner.next is not None:
                print(f"Current data: {current.data}")
                print(f"Runner data: {runner.data}")
                if current.data == runner.next.data:
                    print(f" Inside if ")
                    runner.next = runner.next.next
                    #prev.next = runner.next
                else:
                    print(f" Inside else")
                    runner = runner.next
            current = current.next






l = LinkedList()
l.insert_node(10)
l.insert_node(20)
l.insert_node(30)
l.insert_node(10)
l.insert_node(40)
l.insert_node(50)


print(l.display_nodes())
l.remove_duplicates_wo_addl_ds()
print(l.display_nodes())




