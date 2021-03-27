def fibonacci(n):

    """

    :param n: fibonacci range
    :return:
    """

    if n == 1:
        return 1
    
    a = 0
    b = 1
    count = 0
    while count < n:
        c = a + b
        a, b = b, c
        print(c)
        count += 1
        

#fibonacci(10)

def fib_recursive(n):
    # base case
    if n < 1:
        return 0
    elif n == 1:
        return 1
    
    return fib_recursive(n-1) + fib_recursive(n-2)


#print(fib_recursive(10))


def fib_gen(n):

    a = 0
    b = 1
    count = 0
    while count < n:
        c = a + b
        a,b = b, c
        yield c
        count += 1


myfib = fib_gen(10)
#print(next(myfib))
#print(next(myfib))


def fib_pythonic(n):

    fib_list = [0, 1]
    for i in range(n):
        fib_list.append(fib_list[-1] + fib_list[-2])

    print(fib_list)


#fib_pythonic(10)


def string_check(s):

    if len(s) <= 1:
        return True

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False

    return True


# print(string_check("aac"))


def string_check_with_storage(s):

    if len(s) <= 1:
        return True

    char_dict = dict()

    for i in s:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1

    for k,v in char_dict.items():
        if v > 1:
            return False

    return True


#print(string_check("abcdefghijkl"))


def URLify(s):

    char_list = list()
    
    stripped_str = s.rstrip()
    
    for i in stripped_str:
        if i == " ":
            char_list.append("%20")
        else:
            char_list.append(i)
            
    print("".join(char_list))
            

#URLify("Mr John Smith   ")


def check_str_perm(s1, s2):

    if len(s1) != len(s2):
        return False

    if s1 == s2:
        return True
    
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    
    if sorted_s1 == sorted_s2:
        return True
    return False


#print(check_str_perm("godd", "god"))


def check_str_perm_dict(s1, s2):

    if len(s1) != len(s2):
        return False

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

    if s1_dict == s2_dict:
        return True

    return False

#print(check_str_perm_dict("god", "dog"))


class Node():

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def insert_node(self, data):

        node = Node(data)
        node.next = self.head
        self.head = node


    def display_node(self):
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next

    def remove_duplicates(self):

        buffer_lst = list()
        current = self.head
        prev = self.head
        while current:
            if current.data in buffer_lst:
                prev.next = current.next
            else:
                buffer_lst.append(current.data)
            prev = current
            current = current.next


# l = LinkedList()
# l.insert_node(10)
# l.insert_node(20)
# l.insert_node(30)
# l.insert_node(40)
# l.insert_node(50)
# l.insert_node(10)
# l.insert_node(10)
# l.display_node()
# l.remove_duplicates()
# print()
# l.display_node()

def two_sum(n,target):
    
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i] + n[j] == target:
                print(i, j)
                return 
            
            
# two_sum([2,7,11,15],9)
# two_sum([3,2,4],6)

def valid_paren(s):

    pairs = {"{": "}",
             "[": "]",
             "(": ")"}

    stack = list()

    for ch in s:
        if ch in pairs:
            stack.append(ch)
        else:
            if not stack:
                return False
            else:
                if ch != pairs[stack.pop(ch)]:
                    return False

        return not stack


print(valid_paren("()"))


def remove_duplicates(nums):

    count = 0

    for i in range(len(nums)-1):
        if nums[count] == nums[count+1]:
            nums.remove(nums[count])
        else:
            count += 1

    print(nums)


# remove_duplicates([0,0,1,1,1,2,2,3,3,4])

def long_sub(s):

    result = list()
    length = 0

    for i in s:
        if i in result:
            result = result[result.index(i) + 1:]

        result.append(i)
        print(result)
        length = max(len(result), length)

    print(length)
    
long_sub("bbbbb")



