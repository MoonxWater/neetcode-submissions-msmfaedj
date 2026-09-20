# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
create two var -> ahead and behind
ahead will be n nodes ahead of behind
save the prev node in prev
when ahead reaches end ie ahead.next == None
    we got the node to remove at behind
take the prev node and connect its next with behind.next
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        behind = ahead = prev = head
        cnt = 0

        for i in range(n - 1):
            cnt += 1
            ahead = ahead.next

        while ahead.next:
            cnt += 1
            prev = behind
            behind = behind.next
            ahead = ahead.next

        if n > cnt:
            return head.next

        prev.next = behind.next

        return head
        