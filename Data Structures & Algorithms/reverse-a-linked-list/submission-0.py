# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next = curr.next      # Save next
            curr.next = prev      # Reverse pointer
            prev = curr           # Advance prev
            curr = next           # Advance curr

        return prev

