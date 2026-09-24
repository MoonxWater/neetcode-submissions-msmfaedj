# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
max value of carry is 1;
iterate over the linked list while always storing the prev node;
do the usual addition digit by digit;
set an anchor at a certain node right before a node with value 9;
if a chain of 9s start, we have an anchor to back propogate the carry;
else if the node val is less than 9, move the anchor there
"""
class Solution:
    def get_size(self, l: ListNode) -> int:
        size = 0
        while l:
            size += 1
            l = l.next
        return size
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1, len2 = self.get_size(l1), self.get_size(l2)

        dummy = ListNode()
        prev = anchor = dummy
        carry = 0

        while l1 or l2:
            if l1 and len1 < len2:
                l1_val = 0
                len1 += 1
            elif l1: # case: l1 is not None but len1 >= len2
                l1_val = l1.val
                l1 = l1.next
            else: l1_val = 0 # case: l1 is None

            if l2 and len2 < len1:
                l2_val = 0
                len2 += 1

            elif l2: # case: l2 is not None but len2 >= len1
                l2_val = l2.val
                l2 = l2.next
            else: l2_val = 0 # case: l2 is None

            # the usual
            res = l1_val + l2_val
            carry = res // 10
            digit = res % 10
            prev.val += carry

            if prev.val > 9:
                prev.val %= 10

                while anchor is not prev:
                    anchor.val += 1
                    anchor.val %= 10
                    anchor = anchor.next

                anchor = prev
                
            elif prev.val < 9: anchor = prev

            temp = ListNode(digit)
            prev.next = temp
            prev = temp


        return dummy if dummy.val else dummy.next
