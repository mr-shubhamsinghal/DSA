# Create a binary tree from level order traversal.

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

Q = deque()

def insert_node(data, root):
    
    if data != -1:
        new_node = Node(data)
    else:
        new_node = None
    if Q:
        temp = Q[0]
    if root == None:
        root = new_node
    elif temp.left == None:
        temp.left = new_node
    elif temp.right == None:
        temp.right = new_node
        Q.popleft()
    
    Q.append(new_node)
    return root


def create_binary_tree(arr, root):
    for i in range(len(arr)):
        root = insert_node(arr[i], root)
    return root


def level_order(root):
    
    if not root:
        return
    
    q = deque()
    q.append(root)
    while q:
        temp = q.popleft()
        print(temp.val, end=" ")
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    print()


arr = [1, 2, 3, 4, -1, 5, -1, -1, -1, -1, -1]
root = None
root = create_binary_tree(arr, root)

level_order(root)
