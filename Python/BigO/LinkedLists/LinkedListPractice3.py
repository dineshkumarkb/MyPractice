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
        linked_lst = list()
        while current is not None:
            linked_lst.append(current.data)
            #print(current.data)
            current = current.next
        print(linked_lst)

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

    def get_kth_node(self, k):

        current = self.head
        runner = self.head

        for i in range(k):
            current = current.next

        while current is not None:
            current = current.next
            runner = runner.next

        print(runner.data)

    def partition_list(self, data):

        current = self.head
        runner = self.head

        while current:
            next_node = current.next
            print(f" Comparing {current.data} and {data}")
            if current.data < data:
                current.next = self.head
                self.head = current
                print(f" Current.next {current.next.data}")
                print(f" Head data {self.head.data}")
            else:
                print(f" The current value is {current.data} ")
                print(f" The runner old value is {runner.data} ")
                runner.next = current
                print(f" The runner next data before: {runner.next.data}")
                runner = current
                print(f" The runner new value is {runner.data}")
                print(f" The runner next  value is {runner.next.data}")
            #print(f" Assinging current to {next_node.data}") 
            current = next_node

        runner.next = None

        return self.head

    # def delete_node(self, node):
    #
    #     print(f" Inside delete node: {node} ")
    #
    #     if node is None or node.next is None:
    #         return None
    #
    #     current = node
    #     print(f" Current is: {current.data}")
    #     next_node = node.next
    #     print(f"Next is : {next_node.data}")
    #
    #     current.data = next_node.data
    #     current.next = next_node.next

l = LinkedList()
l.insert_element(1)
l.insert_element(2)
l.insert_element(8)
l.insert_element(2)
l.insert_element(10)
l.insert_element(5)
l.insert_element(3)
#l.display_list()
l.display_list()
print()
l.partition_list(5)
l.display_list()
#l.get_kth_node(3)
#l.remove_duplicates_buffer()
#l.remove_duplicates_wo_buffer()
#print()
#l.display_list()



