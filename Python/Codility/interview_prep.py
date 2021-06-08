def fibonacci(n):

    """

    :param n: fibonacci range
    :return:
    """

    if n == 1:
        return 1

    a = 0
    b = 1
    count = 1
    while count < n:
        c = a + b
        a, b = b, c
        print(c, end=" ")
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

# print(next(myfib))
# print(next(myfib))
# print(next(myfib))
# print(next(myfib))

# for i in myfib:
#     print(i)


def fib_pythonic(n):

    fib_list = [0, 1]
    for i in range(n):
        fib_list.append(fib_list[-1] + fib_list[-2])

    print(fib_list)


# fib_pythonic(10)

class Fibonacci(object):

    def __init__(self, n):
        self.n = n
        self.a = 0
        self.b = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.count < self.n:
            c = self.a + self.b
            self.a, self.b = self.b, c
            self.count += 1
            return c
        else:
            raise StopIteration


# f = Fibonacci(10)
# for i in f:
#     print(i)

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

    def get_kth_node(self,k):

        p1 = self.head
        p2 = self.head

        for i in range(k):
            p1 = p1.next

        while p1:
            p1 = p1.next
            p2 = p2.next

        print(p2.data)




l = LinkedList()
l.insert_node(10)
l.insert_node(20)
l.insert_node(30)
l.insert_node(40)
l.insert_node(50)
# l.insert_node(10)
# l.insert_node(10)
#l.display_node()
#l.remove_duplicates()
#print()
#l.get_kth_node(3)
#l.display_node()

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


#print(valid_paren("()"))


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
            print(f" Inside if condition : {i}")
            print(result)
            result = result[result.index(i) + 1:]
            print(result)

        result.append(i)
        length = max(len(result), length)

    print(length)
    
#long_sub("abcabcbb")


def remove_duplicates_from_sorted_lst(lst):

    count = 0

    for i in range(len(lst)-1):
        if lst[count] == lst[count + 1]:
            lst.remove(lst[count])
        else:
            count += 1

    print(lst)


#remove_duplicates_from_sorted_lst([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])


def search_insert_position(nums, target):

    value = 0

    for i in range(len(nums)):
        if nums[i] == target:
            value = i
            return value
        elif target < nums[i]:
            value = i
            return value
        elif target > nums[-1]:
            return len(nums)
        else:
            return 0
        
    # return value

#print(search_insert_position([1,3,5,6], 7))


def remove_element(nums, target):
    count = 0
    for i in range(len(nums)):
        if nums[count] == target:
            nums.remove(nums[count])
        else:
            count += 1

    print(nums)
    
#remove_element([3,2,2,3], target=3)


def last_word(s):
    if not s.strip():
        return 0
    word_list = s.split()
    word = word_list[-1]
    if word:
        return len(word)
    else:
        return 0


#print(last_word(" "))


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def insert_node(self, data):

        node = Node(data)
        node.next = self.head
        self.head = node

    def display(self):

        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
            

# l = LinkedList()
# l.insert_node(10)
# l.insert_node(20)
# l.insert_node(30)
# l.insert_node(50)
# l.display()



def plus_one(digits):

    joined_str = "".join(map(str,digits))
    incremented_int = int(joined_str) + 1
    return [int(x) for x in str(incremented_int)]


#print(plus_one([1,2,3]))

def remove_element(nums, target):

    count = 0

    for i in range(len(nums)-1):
        if nums[i] == target:
            nums.remove(nums[count])
        else:
            count += 1

    print(nums)


remove_element([3,2,2,3], 3)
