# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_size(self, l: ListNode) -> int:
        size = 0
        while l:
            size += 1
            l = l.next
        return size

    def createNode(self, prev: ListNode, digit: int) -> ListNode:
        temp = ListNode(digit)
        prev.next = temp

        return temp

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1, len2 = self.get_size(l1), self.get_size(l2)

        head = ListNode()
        prev = anchor = head
        carry = 0

        while l1: # or l2; either is fine as we pad the smaller
            if len1 < len2:
                len1 += 1

                l2_val = l2.val
                l2 = l2.next

                prev = self.createNode(prev, l2_val)

                if l2_val < 9: anchor = prev
                continue
            elif len1 > len2:
                len2 += 1

                l1_val = l1.val
                l1 = l1.next

                prev = self.createNode(prev, l1_val)

                if l1_val < 9: anchor = prev
                continue

        
            l1_val = l1.val
            l1 = l1.next

            l2_val = l2.val
            l2 = l2.next

            # the usual
            res = l1_val + l2_val
            digit = res % 10
            carry = res // 10

            prev.val += carry

            # carry propagation
            if prev.val > 9:
                prev.val %= 10

                while anchor is not prev:
                    anchor.val += 1
                    anchor.val %= 10
                    anchor = anchor.next

                anchor = prev
            elif prev.val < 9: anchor = prev

            prev = self.createNode(prev, digit)


        return head if head.val else head.next