class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insert_node(self, val):

        node = ListNode(val)
        node.next = self.head
        self.head = node






l1 = LinkedList()
l1.insert_node(3)
l1.insert_node(4)
l1.insert_node(2)

l2 = LinkedList()
l2.insert_node(4)
l2.insert_node(6)
l2.insert_node(5)


def add_two_numbers(l1, l2):
    lst1 = list()
    lst2 = list()

    current1 = l1.head
    current2 = l2.head

    while current1:
        lst1.append(str(current1.val))
        current1 = current1.next

    while current2:
        lst2.append(str(current2.val))
        current2 = current2.next

    converted_lst1 = "".join(lst1)
    converted_lst2 = "".join(lst2)

    added_val = int(converted_lst1) + int(converted_lst2)
    final_int = list(str(added_val))
    final_int.reverse()
    lst2LL(final_int)

def lst2LL(l):

    current = dummy = ListNode()

    for i in l:
        current.next = ListNode(int(i))
        current = current.next

    print(dummy.next.val)

    
add_two_numbers(l1, l2)
