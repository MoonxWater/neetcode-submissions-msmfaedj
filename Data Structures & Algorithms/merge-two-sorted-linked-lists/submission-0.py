# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        elif not list2:
            return list1
        
        cur_node = prev = None
        flag = True
        head = None

        while list1 and list2:
            if list1.val <= list2.val:
                cur_node = ListNode(list1.val)
                list1 = list1.next  
            else:
                cur_node = ListNode(list2.val)
                list2 = list2.next

            if flag == True:
                head = cur_node
                flag = False

            else:
                prev.next = cur_node
            
            prev = cur_node

        if list1:
            prev.next = list1

        else:
            prev.next = list2

        return head