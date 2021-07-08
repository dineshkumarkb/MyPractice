class Node:
    """
    A Node class which contains the data
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        # We have a current value to always point to the last node
        self.current = None

    def insert_at_the_end(self, data):
        """
        The insertion here is performed with a time complexity of O(1)
        :param data:
        :return:
        """

        if not data:
            return

        # Initialize the node object
        node = Node(data)

        # Insertion for the first/head element
        if not self.head:
            node.next = self.head
            self.head = node
            self.current = self.head
        # Insertion for non head elements using current object
        else:
            self.current.next = node
            self.current = self.current.next

    def get_lst_head(self):
        """
        A method to return the head
        :return:
        """
        return self.head


def print_lst(head):

    current = head

    while current:
        print(current.data, end="->")
        current = current.next


def reverse_lst(head):

    current = head
    new_head = None

    while current:
        node = Node(current.data)
        # Assign the new head to node's next
        node.next = new_head
        # Assign the node to new head
        new_head = node
        current = current.next

    return new_head






l1 = LinkedList()
l1.insert_at_the_end(10)
l1.insert_at_the_end(20)
l1.insert_at_the_end(30)
l1.insert_at_the_end(40)

l1_head = l1.get_lst_head()

print_lst(l1_head)
print()
reversed_head = reverse_lst(l1_head)
print_lst(reversed_head)


