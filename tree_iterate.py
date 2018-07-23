import collections
import sys

class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    
    def validate_BST_Itr(self,root):
        """
        this is an iterative, as opposed to recursive, method to validate that a Binary Search Tree is of proper form
        Basically it's a wrapper class that keeps track of what the current highest and lowest value should be


        """

        queue=collections.deque()  # deque is a double ended queue
        queue.append(TreeBoundaryNode(root,-sys.maxsize+1, sys.maxsize-1))
        
        while (queue):
            cur=queue.popleft()
            node=cur.root
            if node.data < cur.left_boundary or node.data > cur.right_boundary:
                return False
            if node.left_child is not None:
                queue.append(TreeBoundaryNode(node.left_child, cur.left_boundary, node.data))
            if node.right_child is not None:
                queue.append(TreeBoundaryNode(node.right_child, node.data, cur.right_boundary))
        return True

class TreeBoundaryNode:
    def __init__(self, root_node, left_boundary, right_boundary):
        self.root = root_node
        self.left_boundary=left_boundary
        self.right_boundary=right_boundary


class TreeNode:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

TESTMODE=0
if TESTMODE:

#    a=TreeNode(4)
#    a.left_child=TreeNode(3)
#    a.right_child=TreeNode(5)

    a=TreeNode(20)
    a.left_child=TreeNode(15)
    a.left_child.right_child=TreeNode(18)
    a.right_child=TreeNode(30)
    a.right_child.right_child=TreeNode(40)

    tree=BinaryTree(a)

    tree.validate_BST_Itr(tree.root)
