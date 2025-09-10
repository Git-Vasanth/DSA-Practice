

class Node(object):

    def __init__(self , d , n = None):
        
        self.data = d

        self.next_node = n

    def get_data(self):

        return self.data
    
    def set_data(self , d):

        self.data = d

    def get_next_node(self):

        return self.next_node
    
    def set_next_node(self , n):

        self.next_node = n

    def __str__(self) :
        
        return str(self.data)


Head = Node(1)

elem_1 = Node(2)

elem_2 = Node(3)

elem_3 = Node(4)

Head.next_node = elem_1
elem_1.next_node = elem_2
elem_2.next_node = elem_3

current = Head

linked_list = []

while current:

    linked_list.append(str(current.data))

    current = current.next_node

print(' -> '.join(linked_list))

