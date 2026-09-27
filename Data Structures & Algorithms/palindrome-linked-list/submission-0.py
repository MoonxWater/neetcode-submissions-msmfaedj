# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []
        slow = fast = head

        while fast:
            if fast.next:
                fast = fast.next.next
                s.append(slow.val)
            else:
                fast = fast.next
            slow = slow.next

        while slow:
            if s.pop() != slow.val:
                return False
            slow = slow.next

        return True