class ListNode:

    def __init__(self, data):
        self.val = data
        self.next = None


def make_lst(elements):

    head = ListNode(elements[0])
    current = head
    for i in elements[1:]:
        while current.next:
            current = current.next
        current.next = ListNode(i)

    return head

def display_lst(head):

    current = head

    while current:
        print(current.val, end="->")
        current = current.next

class Solution:

    def add_two_numbers(self, l1:ListNode, l2:ListNode):

        head = None
        temp = None
        carry = 0

        while l1 or l2:

            if not l1:
                a = 0
            else:
                a = l1.val

            if not l2:
                b = 0
            else:
                b = l2.val

            n = a + b + carry

            if n > 9:
                carry = 1
            else:
                carry = 0

            node = ListNode(n % 10)

            if not head:
                head = node
                temp = node
            else:
                head.next = node
                head = node

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        if carry:
            node = ListNode(carry)
            head.next = node

        return temp


obl = Solution()
l1 = make_lst([9,9,9,9,9,9,9])
l2 = make_lst([9,9,9,9])
display_lst(obl.add_two_numbers(l1, l2))
