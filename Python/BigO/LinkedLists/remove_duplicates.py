class Node(object):
    """
    This is a Node class.
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert_node(self, data):
        """
        :param data: Node data
        :return: None
        """
        node = Node(data)
        node.next = self.head
        self.head = node

    def display_list(self):

        current = self.head
        while current:
            print(current.value, end="->")
            current = current.next

    def delete_duplicates(self):

        current = self.head
        # This is require to keep track of the prev Node
        prev = None
        duplicate_dict = dict()
        while current:
            if current.value not in duplicate_dict:
                duplicate_dict[current.value] = None
                # Track the prev Node
                prev = current
            else:
                # When a duplicate is found assign prev Node's next to current's next
                prev.next = current.next

            current = current.next

    def delete_duplicates_2(self):

        current = self.head

        while current:
            runner = current
            # Check until runner.next is not None.
            while runner.next:
                if current.value == runner.next.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next







l = LinkedList()
l.insert_node(25)
l.insert_node(35)
l.insert_node(15)
l.insert_node(32)
l.insert_node(25)
l.insert_node(80)
l.insert_node(15)
l.display_list()
#l.delete_duplicates()
l.delete_duplicates_2()
print()
l.display_list()