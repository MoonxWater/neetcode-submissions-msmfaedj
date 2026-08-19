# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
            
        i = cur_node = head
        j = head.next
        speed = 0

        while cur_node.next:
            i = cur_node
            temp = cur_node

            for k in range(speed):
                if temp.next:
                    j = temp.next
                    temp = temp.next

            cur_node = cur_node.next
            speed += 1

            if i == j:
                return True
        
        return False
        