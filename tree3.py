class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if root is not None:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root


root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
inverted_root1 = invertTree(root1)
print(inverted_root1.val)  
print(inverted_root1.left.val) 
print(inverted_root1.right.val)  
print(inverted_root1.left.left.val) 
print(inverted_root1.left.right.val) 
print(inverted_root1.right.left.val)  
print(inverted_root1.right.right.val)  

