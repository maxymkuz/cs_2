class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def __str__(self):
        return self.value


def print_linked(root):
    s = ""
    while root.next is not None:
        s += str(root)
        root = root.next
    s += str(root)
    print(s)


def len_linked(root):
    length = 1
    while root.next is not None:
        length += 1
        root = root.next
    return length


# def insert_node(root, value, index):
#     idx = 0
#     new = Node(value)
#     if index < 0 or index >= len_linked(root):
#         raise IndexError
#     if index == 0:
#         new.next = root
#         return new
#
#     while True:
#         if idx == index:
#             new.next = root.next
#             root.next = new
#             break
#         root = root.next
#         idx += 1


def insert_node(root, value, index):
    new = Node(value)
    if index == 0:
        new.next = root
        return new
    if index < 0 or index > len_linked(root):
        raise IndexError

    node = root
    for _ in range(index - 1):
        node = node.next
    new.next = node.next
    node.next = new
    return root


n1 = Node(' red ')
n2 = Node(' yhkjnkj ')
n3 = Node(' hhhhhhh ')

n3.next = n1
n1.next = n2

x = insert_node(n3, '   asdas  ', 3)
print_linked(x)
