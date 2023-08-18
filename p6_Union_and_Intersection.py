class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, length=0):
        self.head = None
        self.length = length

    def insert_node(self, value, length=1):
        node = Node(value, self.head)
        self.head = node
        self.length = length


def display_list(list):
    temp = list
    while temp:
        print(temp.value, end="\t")
        temp = temp.next
    print("")


def check_list(list, value):
    temp = list
    while temp:
        if temp.value is value:
            return True
        temp = temp.next
    return False


def union(list1, list2):
    union = LinkedList()
    temp = list1
    while temp:
        union.insert_node(temp.value)
        temp = temp.next

    temp = list2
    while temp:
        if not check_list(union.head, temp.value):
            union.insert_node(temp.value)
        temp = temp.next
    return union.head


def intersection(list1, list2):
    intersection = LinkedList()
    temp = list1
    while temp:
        if check_list(list2, temp.value):
            intersection.insert_node(temp.value)

    return intersection.head

list1 = LinkedList()
list1.insert_node(5)
list1.insert_node(6)
list1.insert_node(7)
list1.insert_node(8)
list1.insert_node(9)
list1.insert_node(10)
# print("Linked list 1: ")
# display_list(list1.head)

list2 = LinkedList()
list2.insert_node(0)
list2.insert_node(1)
list2.insert_node(2)
list2.insert_node(3)
list2.insert_node(4)
# print("Linked list 2: ")
# display_list(list2.head)

print("The union of lists 1 and 2 is: ")
union = union(list1.head, list2.head)
display_list(union)