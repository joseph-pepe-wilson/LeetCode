from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        pair = [float('-inf') , -1]
        max_sum = float('-inf')
        level = 0
        while q:
            size = len(q)
            level_sum = 0
            for _ in range(size):
                node = q[0]
                q.popleft()
                level_sum+=node.val
                if node.left :
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level+=1
            if level_sum > max_sum:
                max_sum = level_sum
                pair[0] = level_sum
                pair[1] = level
        return pair[1] 