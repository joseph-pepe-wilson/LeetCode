# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        tot = 0
        stack = [(root,str(root.val))]
        while stack:
            node, binVal = stack.pop()
            if node.left:
                stack.append((node.left,binVal+str(node.left.val)))
            if node.right:
                stack.append((node.right,binVal+str(node.right.val)))
            if not node.left and not node.right:
                tot += int(binVal,2)
        return tot