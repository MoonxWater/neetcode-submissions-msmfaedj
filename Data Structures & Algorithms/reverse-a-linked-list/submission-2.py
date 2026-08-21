# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cursor = head
        prev = None

        while cursor:
            nxt = cursor.next
            cursor.next = prev
            prev = cursor
            cursor = nxt
        
        return prev