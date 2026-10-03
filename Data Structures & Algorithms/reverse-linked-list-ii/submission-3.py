# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
|1  2  3|  4 5 ->>> 1->4, dummy->1, start= dummy
1 2  |3  4  5|  6 7 8 ->>> 2->5, 3->6, start=2
1 2  |3  4| ->>> 2->4, 3->None, start= 2
"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        right = right - left + 1

        while left := left - 1:
            prev, cur = cur, cur.next

        start = prev
        end = cur

        while right and cur:
            right -= 1

            next_node = cur.next
            cur.next = prev
            prev = cur

            cur = next_node 

        end.next = cur
        start.next = prev
        
        return dummy.next