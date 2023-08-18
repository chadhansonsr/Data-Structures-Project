class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_node(self, value):
        node = Node(value, self.head)
        self.head = node
        self.length = 1


def display_list(list):
    temp = list
    while temp:
        print(temp.value, end="\t")
        temp = temp.next
    print("")

def check_list( list, value):
    temp = list
    while temp:
        if temp.value == value:
            return True
        temp = temp.next
    return False

def union(list1, list2):
    dict = {}
    union = LinkedList()
    temp = list1
    while temp:
        union.insert_node(temp.value)
        dict[temp.value] = 1
        temp = temp.next

    temp = list2
    while temp:
        if (dict.get(temp.value, None) == None):
            union.insert_node(temp.value)
        temp = temp.next
    return union.head


def intersection(list1, list2):
    dict = {}
    intersection = LinkedList()
    temp = list1
    while temp:
        dict[temp.value] = 1
        temp = temp.next

    temp = list2
    while temp:
        if dict.get(temp.value, None):
            intersection.insert_node(temp.value)
        temp = temp.next
    return intersection.head


list1 = LinkedList()
list1.insert_node(3)
list1.insert_node(2)
list1.insert_node(4)
list1.insert_node(35)
list1.insert_node(6)
list1.insert_node(65)
list1.insert_node(6)
list1.insert_node(4)
list1.insert_node(3)
list1.insert_node(21)
print("Linked list 1: ")
display_list(list1.head)

list2 = LinkedList()
list2.insert_node(6)
list2.insert_node(32)
list2.insert_node(4)
list2.insert_node(9)
list2.insert_node(6)
list2.insert_node(1)
list2.insert_node(11)
list2.insert_node(21)
list2.insert_node(1)
print("Linked list 2: ")
display_list(list2.head)

union1 = union(list1.head, list2.head)
print("\n\nThe union of lists 1 and 2 is: ")
display_list(union1)

intersection1 = intersection(list1.head, list2.head)
print("The intersection of lists 1 and 2 is: ")
display_list(intersection1)


# list3 = LinkedList()
# list3.insert_node(4)
# list3.insert_node(6)
# list3.insert_node(4)
# list3.insert_node(8)
# list3.insert_node(9)
# list3.insert_node(10)
# print("\n\nLinked list 3: ")
# display_list(list3.head)

# list4 = LinkedList()
# list4.insert_node(0)
# list4.insert_node(1)
# list4.insert_node(2)
# list4.insert_node(8)
# list4.insert_node(4)
# print("Linked list 4: ")
# display_list(list4.head)

# union2 = union(list3.head, list4.head)
# print("\n\nThe union of lists 3 and 4 is: ")
# display_list(union2)

# intersection2 = intersection(list3.head, list4.head)
# print("The intersection of lists 3 and 4 is: ")
# display_list(intersection2)
