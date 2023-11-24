class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minCameraCover(root):
    def dfs(node, cameras):
        if not node:
            return 2

        left = dfs(node.left, cameras)
        right = dfs(node.right, cameras)

        if left == 0 or right == 0:
            cameras[0] += 1
            return 1

        if left == 2 and right == 2:
            return 0

        return 2

    cameras = [0]
    if dfs(root, cameras) == 0:
        cameras[0] += 1

    return cameras[0]

root1 = TreeNode(0, None, TreeNode(0, None, TreeNode(0)))
print(minCameraCover(root1))  

root2 = TreeNode(0, None, TreeNode(0, None, TreeNode(0, None, TreeNode(0))))
print(minCameraCover(root2))  
