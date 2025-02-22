# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: Optional[TreeNode]
        """
        stack = []
        i, n = 0, len(traversal)

        while i < n:
            depth = 0
            # Count the depth (number of dashes)
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1

            # Read the node value
            start = i
            while i < n and traversal[i].isdigit():
                i += 1
            value = int(traversal[start:i])

            node = TreeNode(value)

            # Maintain stack such that it contains only ancestors of the current node
            if depth < len(stack):
                stack = stack[:depth]  # Trim stack to the correct depth
            
            # Attach node to the parent
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            stack.append(node)

        return stack[0]