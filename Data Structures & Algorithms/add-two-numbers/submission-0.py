# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = 0
        i = 0

        while l1:
            num1 += l1.val * 10 ** i
            l1 = l1.next
            i += 1
        i = 0
        while l2:
            num2 += l2.val * 10 ** i
            l2 = l2.next
            i += 1

        res = num1 + num2
        dummy = ListNode(0)
        prev = dummy

        for num in reversed(str(res)):
            cur = ListNode(int(num))
            prev.next = cur
            prev = cur

        return dummy.next
            


        
