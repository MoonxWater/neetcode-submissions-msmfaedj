# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sizer1, sizer2 = l1, l2
        len1 = len2 = 0

        while sizer1 or sizer2:
            if sizer1:
                sizer1 = sizer1.next
                len1 += 1
            if sizer2:
                sizer2 = sizer2.next
                len2 += 1

        dummy = ListNode()
        prev = dummy
        carry = 0
        anchor = dummy

        while l1 or l2:
            if l1:
                if len1 < len2:
                    l1_val = 0
                    len1 += 1
                else: 
                    l1_val = l1.val
                    l1 = l1.next
            else: l1_val = 0

            if l2:
                if len2 < len1:
                    l2_val = 0
                    len2 += 1
                else: 
                    l2_val = l2.val
                    l2 = l2.next
            else: l2_val = 0


            res = l1_val + l2_val
            carry = res // 10
            digit = res % 10

            if carry:
                prev.val += carry
                if prev.val > 9:
                    prev.val %= 10
                    while anchor is not prev:
                        anchor.val += 1
                        anchor.val %= 10
                        anchor = anchor.next
                else:
                    anchor = prev


            temp = ListNode(digit)
            prev.next = temp
            if prev.val < 9: anchor = prev
            prev = temp



        return dummy if dummy.val else dummy.next
