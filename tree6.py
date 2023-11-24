class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    def maxPathSumHelper(node):
        nonlocal max_sum

        if not node:
            return 0

        left_sum = max(0, maxPathSumHelper(node.left))
        right_sum = max(0, maxPathSumHelper(node.right))
        current_sum = node.val + left_sum + right_sum

        max_sum = max(max_sum, current_sum)

        return node.val + max(left_sum, right_sum)

    max_sum = float('-inf')
    maxPathSumHelper(root)
    return max_sum

root1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(maxPathSum(root1))  

root2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(maxPathSum(root2))  
