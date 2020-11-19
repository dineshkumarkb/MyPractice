class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert_node(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def display_all_nodes(self):

        current = self.head
        val_lst = list()
        while current is not None:
            val_lst.append(current.data)
            current = current.next

        return val_lst

    def remove_dup_with_storage(self):
        """
        The time complexity of this is O(n)
        :return:
        """
        current = self.head
        temp_lst = list()
        while current is not None:
            if current.data in temp_lst:
                prev.next = current.next
            else:
                prev = current
                print(f" The prev: {prev.data}")
                temp_lst.append(current.data)
            current = current.next

    def remove_dup_without_storage(self):
        """
        Iteration 1 current = 15, prev = 15
        if 15 == 10
        prev = 10
        Iteration 2 current = 15, prev = 10
        if 15 == 15

        :return:
        """
        current = self.head
        while current is not None:
            prev = current
            while prev.next is not None:
                if current.data == prev.next.data:
                    prev.next = prev.next.next
                else:
                    prev = prev.next
            current = current.next


"""
Compare adjacent elements in the linked list. Have 2 pointers..one is current..one is a either a step
after current or a step before current.
Iteration 1 : prev = None, current =15 15 not in templst. prev = 15 current = 10
Iteration 2: prev = 15, current = 10 10 not in templst.
"""

l = LinkedList()
l.insert_node(10)
l.insert_node(20)
l.insert_node(15)
l.insert_node(10)
l.insert_node(15)
print(l.display_all_nodes())
l.remove_dup_with_storage()
#l.remove_dup_without_storage()
print(l.display_all_nodes())

