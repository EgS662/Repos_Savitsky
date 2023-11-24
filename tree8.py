class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalTraversal(root):
    if not root:
        return []

    column_table = {}
    min_col, max_col = float('inf'), float('-inf')
    stack = [(root, 0, 0)]

    while stack:
        node, row, column = stack.pop()
        if column in column_table:
            column_table[column].append((row, node.val))
        else:
            column_table[column] = [(row, node.val)]

        min_col = min(min_col, column)
        max_col = max(max_col, column)

        if node.right:
            stack.append((node.right, row + 1, column + 1))
        if node.left:
            stack.append((node.left, row + 1, column - 1))

    result = []
    for col in range(min_col, max_col + 1):
        if col in column_table:
            result.append([val for row, val in sorted(column_table[col])])

    return result

root1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(verticalTraversal(root1)) 

root2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(verticalTraversal(root2))  

