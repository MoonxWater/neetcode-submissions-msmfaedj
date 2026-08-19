# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
val0  -  val1  -  val2  -  val3
val1  -  val2  -  val3  -  None

val0  -  val1  -  val2  -  val3
None  -  val0  -  val1  -  val2

temp_prev -> prev one
temp_next -> next one

Step 1: only for head: save next in temp_next and update next to  None save the current to temp_prev and use temp_next to move on

Step 2: save next to temp_next and update next to temp_prev
update temp_prev with the current obj and use temp_next to move on

Step 3: only for last:
'''


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cursor = head

        while cursor:
            nxt = cursor.next
            cursor.next = prev
            prev = cursor
            cursor = nxt

        return prev