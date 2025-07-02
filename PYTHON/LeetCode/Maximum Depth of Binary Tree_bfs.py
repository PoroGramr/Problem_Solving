from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        q = deque()
        q.append((root,1))

        depth = 0

        while q:
            cur_node, cur_depth = q.popleft()

            depth = max(depth, cur_depth)

            if cur_node.left:
                q.append((cur_node.left, cur_depth + 1))
            
            if cur_node.right:
                q.append((cur_node.right, cur_depth + 1))

        
        return depth
