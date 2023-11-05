class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []
    
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
    
    traverse(root)
    return result

root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(inorderTraversal(root1))  

root2 = None
print(inorderTraversal(root2)) 

root3 = TreeNode(1)
print(inorderTraversal(root3))