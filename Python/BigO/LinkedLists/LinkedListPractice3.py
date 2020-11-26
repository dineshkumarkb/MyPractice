class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert_element(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def display_list(self):

        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def remove_duplicates_buffer(self):

        buffer = list()
        current = self.head
        prev = self.head

        while current is not None:
            print(f" Comparing {current.data}")
            if current.data in buffer:
                prev.next = current.next
            else:
                buffer.append(current.data)
                prev = current
            current = current.next

    def remove_duplicates_wo_buffer(self):

        current = self.head

        while current is not None:
            prev = current
            while prev.next is not None:
                if current.data == prev.next.data:
                    prev.next = prev.next.next
                else:
                    prev = prev.next
            current = current.next


l = LinkedList()
l.insert_element(10)
l.insert_element(20)
l.insert_element(30)
l.insert_element(10)
l.insert_element(30)
l.display_list()
#l.remove_duplicates_buffer()
l.remove_duplicates_wo_buffer()
print()
l.display_list()
