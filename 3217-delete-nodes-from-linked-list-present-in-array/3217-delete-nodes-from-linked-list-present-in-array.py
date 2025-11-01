from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums to a set for O(1) lookup
        remove_set = set(nums)

        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head

        # Use two pointers: prev and current
        prev, current = dummy, head

        while current:
            if current.val in remove_set:
                # Skip the current node
                prev.next = current.next
            else:
                # Move prev forward only if current is not removed
                prev = current
            current = current.next

        return dummy.next