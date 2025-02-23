# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.

class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not postorder:
            return None

        root = TreeNode(preorder[0])  
        if len(preorder) == 1:
            return root  

        left_subtree_root = preorder[1]  
        left_size = postorder.index(left_subtree_root) + 1 

        root.left = self.constructFromPrePost(preorder[1:left_size+1], postorder[:left_size])
        root.right = self.constructFromPrePost(preorder[left_size+1:], postorder[left_size:-1])

        return root

        