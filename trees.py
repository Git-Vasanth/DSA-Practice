class Tree_Node:

    def __init__(self , value = 0) -> None:
        
        self.value = value

        self.left = None

        self.right = None

A = Tree_Node(9)
B = Tree_Node(10)
C = Tree_Node(10)

A.left = B
A.right = C


def is_symmentric(root):

    if root is None:
        return True

    def is_mirror(root_left ,root_right):

        if root_left == None and root_right == None:
            return True
        
        if root_left == None or root_right == None:
            return False
        
        if root_left.value != root_right.value:
            return False
        
        return is_mirror(root_left.left , root_right.right) and is_mirror(root_left.right , root_right.left)
    
    
    return is_mirror(root.left , root.right)


print(is_symmentric(A))