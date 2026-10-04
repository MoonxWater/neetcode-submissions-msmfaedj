"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
            
        node_map = {}
        cur = head

        while cur:
            node = Node(cur.val)
            node_map[cur] = node
            cur = cur.next

        cur = head

        while cur:
            node_map[cur].next = node_map.get(cur.next)
            node_map[cur].random = node_map.get(cur.random)
            cur = cur.next
        
        return node_map[head]
