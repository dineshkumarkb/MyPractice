class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert_node(self, data):

        if not data:
            return

        n = Node(data)
        n.next = self.head
        self.head = n

    def add_node(self, node):

        if not node:
            return

        node.next = self.head
        self.head = node

    def display_lst(self, lst_object):

        if not lst_object:
            return

        current = lst_object.head

        while current:
            print(current.data, end="->")
            current = current.next

    def display_nodes(self, lst_object):
        if not lst_object:
            return

        current = lst_object.head

        nodes_lst = list()

        while current:
            #print(current)
            nodes_lst.append(current)
            current = current.next

        return nodes_lst

    def check_intersection(self, l1, l2):

        lst1_length = self.get_ll_length(l1)
        lst2_length = self.get_ll_length(l2)
        print(f" List1 length: {lst1_length}")
        print(f" List2 length: {lst2_length}")
        l1_last_node = self.get_last_node(l1)
        l2_last_node = self.get_last_node(l2)
        if l2_last_node is l1_last_node:
            return True
        return False

    def get_ll_length(self, lst):

        current = lst.head
        count = 1
        while current:
            count += 1
            current = current.next

        return count

    def get_last_node(self,lst):

        current = lst.head
        while current:
            current = current.next

        last_node = current
        return last_node

    def get_kth_node(self, l2, x):

        p1 = l2.head
        p2 = l2.head

        for i in range(x):
            p1 = p1.next

        while p1:
            p1 = p1.next
            p2 = p2.next

        return p2







l1 = LinkedList()
l1.insert_node(1)
l1.insert_node(2)
l1.insert_node(3)
l1.insert_node(4)
#l1.display_nodes(l1)
print()
l2 = LinkedList()
l1_nodes = l1.display_nodes(l1)
l1_nodes.reverse()
for n in l1_nodes:
    l2.add_node(n)
print()
l2.insert_node(5)
l2.insert_node(6)
l2.insert_node(7)
l2.insert_node(8)
l2.insert_node(9)
l2.display_nodes(l2)
l1_length = l1.get_ll_length(l1)
l2_length = l2.get_ll_length(l2)
print(l1_length, l2_length)
diff = abs(l1_length - l2_length)
print(l2.check_intersection(l1, l2))
print(f"diff: {diff}")
print(l2.get_kth_node(l2, diff).data)
print(l1.display_lst(l1))
print(l2.display_lst(l2))

