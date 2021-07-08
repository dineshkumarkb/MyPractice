# Generate fibonacci series

def fib_series(n):

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    fib_lst = [0,1]

    for i in range(n):
        fib_lst.append(fib_lst[-2] + fib_lst[-1])

    return fib_lst


#print(fib_series(2))


# Return fib number

def fib_num(n):

    if n <= 0:
        return 0

    elif n == 1:
        return 1

    a, b = 0, 1

    for i in range(n):
        c = a + b
        a, b = b, c

    return c


#print(fib_num(2))


# Convert a list to a dictionary

my_lst = ["a",1,"b",2,"c",3,"d",4,"e",5]


def convert_lst_to_dict(lst):

    if not lst or not isinstance(lst, list):
        raise ValueError(" Please provide list with values ")

    l1 = my_lst[::2]
    l2 = my_lst[1::2]

    return dict(zip(l1, l2))


#print(convert_lst_to_dict(my_lst))


def convert_lst_to_dict_iter(my_lst):

    if not isinstance(my_lst, list) or not my_lst:
        raise Exception(" Please provide a list with appropriate values ")

    it = iter(my_lst)
    my_dict = dict(zip(it, it))

    return my_dict


#print(convert_lst_to_dict_iter(my_lst))

def convert_lst_to_dict_for(l):

    my_dict = dict()

    # for i in range(0,len(my_lst)-1,2):
    #     my_dict[my_lst[i]] = my_lst[i+1]
    print({l[i]: l[i + 1] for i in range(0, len(l) - 1, 2)})
    #my_dict = {my_lst[i]:my_lst[i+1] for i in range(0,len(my_lst), 2)}
    return my_dict

#print(convert_lst_to_dict_for([1,"a",2,"b",3,"c",4,"d"]))


# Linked list
class Node(object):

    def __init__(self, data= None):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def insert_first(self, data):

        if data is None:
            return

        node = Node(data)
        node.next = self.head
        self.head = node

    def display_nodes(self):

        current = self.head

        while current:
            print(current.data)
            current = current.next


# l = LinkedList()
# l.insert_first(10)
# l.insert_first(20)
# l.insert_first(30)
# l.insert_first(40)
# l.display_nodes()


class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.current = None

    def insert_node_last(self, data):

        if data is None:
            return
        node = Node(data)
        if self.head is None:
            node.next = self.head
            self.head = node
            self.current = self.head

        else:
            self.current.next = node
            self.current = self.current.next

    def display_nodes(self):

        current = self.head
        while current:
            print(current.data)
            current = current.next

# l = LinkedList()
# l.insert_node_last(10)
# l.insert_node_last(20)
# l.insert_node_last(30)
# l.insert_node_last(40)
# l.display_nodes()

my_dict = {"1": "dinesh", "3": "Ramesh", "2": "pete", "4": "emma"}

#print(sorted(my_dict.items(), key=lambda x: x[1].lower()))


def sort_dict_by_values(my_dict):

    lst_values = list()

    for _,v in my_dict.items():
        lst_values.append(v)

    lst_values.sort()

    copy_dict = dict()

    for val in lst_values:
        for k,v in my_dict.items():
            if val == v:
                copy_dict[k] = v

    print(copy_dict)


#sort_dict_by_values(my_dict)

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.current = None

    def insert_at_head(self, data):

        if data is None:
            return

        node = Node(data)

        node.next = self.head
        self.head = node

    def display_nodes(self):

        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next

    def delete_duplicates(self):

        dup_lst = list()
        current = self.head
        prev = self.head

        while current:
            if current.data in dup_lst:
                prev.next = current.next
            else:
                dup_lst.append(current.data)
                prev = current
            current = current.next

    def delete_duplicates_without_buffer(self):

        current = self.head

        while current:
            runner = current
            while runner.next:
                print(f" Comparing {current.data} and {runner.next.data}")
                if current.data == runner.next.data:
                   runner.next = runner.next.next
                else:
                    runner = runner.next

            current = current.next


    def sort_list(self):

        el_lst = list()
        current = self.head

        while current:
            el_lst.append(current.data)
            current = current.next

        el_lst.sort(reverse=True)

        ll = LinkedList()

        for d in el_lst:
            ll.insert_at_head(d)

        ll.display_nodes()



# l = LinkedList()
# l.insert_at_head(23)
# l.insert_at_head(12)
# l.insert_at_head(45)
# l.insert_at_head(23)
# l.insert_at_head(52)
# l.insert_at_head(43)
# l.display_nodes()
# #l.delete_duplicates()
# l.delete_duplicates_without_buffer()
# print()
# # l.sort_list()
# l.display_nodes()


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.current = None

    def insert_node_at_last(self, data):

        if not data:
            return

        node = Node(data)

        if self.head is None:
            node.next = self.head
            self.head = node
            self.current = self.head
        else:
            self.current.next = node
            self.current = self.current.next

    def display_nodes(self):

        current = self.head

        while current:
            print(current.data, end="->")
            current = current.next

    def get_kth_node(self, k):

        current = self.head
        runner = self.head

        for i in range(k):
            runner = runner.next

        while runner:
            current = current.next
            runner = runner.next

        print(current.data)



# l = LinkedList()
# l.insert_node_at_last(10)
# l.insert_node_at_last(20)
# l.insert_node_at_last(30)
# l.insert_node_at_last(40)
# l.display_nodes()
# print()
# l.get_kth_node(2)


def is_unique(s):

    if len(s) > 256:
        return False

    dup_lst = list()

    for c in s:
        if c in dup_lst:
            return False
        else:
            dup_lst.append(c)

    return True


#print(is_unique("abcdae"))


def is_unique_1(s):

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False

    return True


#print(is_unique("abacde"))

def is_permutation(s1, s2):

    if len(s1) != len(s2):
        return False

    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))

    if s1 == s2:
        return True

    return False


#print(is_permutation("godd", "dog"))

def permutation_dict(s1, s2):

    s1_dict = dict()
    s2_dict = dict()

    for c1 in s1:
        if c1 in s1_dict:
            s1_dict[c1] += 1
        else:
            s1_dict[c1] = 1

    for c2 in s2:
        if c2 in s2_dict:
            s2_dict[c2] += 1
        else:
            s2_dict[c2] = 1
    print(s1_dict, s2_dict)
    if s1_dict == s2_dict:
        return True

    return False


#print(permutation_dict("godd", "dog"))

def two_sums(nums, target):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i,j

    return 0


# print(two_sums([3, 2, 4], 6))

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):

        if not data:
            return
        node = Node(data)
        if self.head is None:
            node.next = self.head
            self.head = node
            return

        current = self.head

        if current.data > node.data:
            node.next = current
            self.head = node
            return

        while current.next:
            if current.next.data > data:
                break
            current = current.next

        node.next = current.next
        current.next = node



# Longest substring


def check_perm(s1, s2):

    if s1 is None or s2 is None:
        return

    size = len(s1)

    for i in range(len(s2)):
        window = s2[i:i+size]
        print(window)
        if is_perm(s1, window):
            return True

    return False


def is_perm(s, t):

    if len(s) != len(t):
        return False

    if s == t:
        return True

    from collections import Counter
    s1 = Counter(s)
    t1 = Counter(t)

    return s1 == t1

#print(check_perm("ab","eidbaooo"))


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


def make_lst(elements):

    head = elements[0]

    current = head

    for i in elements[1:]:
        while current.next:
            current = current.next
        current.next = ListNode(i)

    return head


def add_nums(l1, l2):

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

    if carry:
        node = ListNode(carry)
        head.next = node


def stock_prices(price_lst):

    n = len(price_lst)

    i = 0

    while i < n-1:

        while i < n-1 and price_lst[i+1] >= price_lst[i]:
            i += 1


        buy = i
        i += 1

        while i < n and price_lst[i] >= price_lst[i-1]:
            i += 1

        sell = i - 1







