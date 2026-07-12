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
        if not head: return 
        hash_map = {}
    
        cur = head
        while cur:

            hash_map[cur] = hash_map.get(cur, Node(cur.val))
            duplicate = hash_map[cur]

            if cur.next:
                if cur.next not in hash_map:
                    duplicate_next = Node(cur.next.val)
                    hash_map[cur.next] = duplicate_next
                duplicate.next = hash_map[cur.next]
            
            if cur.random:
                if cur.random not in hash_map:
                    duplicate_random = Node(cur.random.val)
                    hash_map[cur.random] = duplicate_random
                duplicate.random = hash_map[cur.random]
            cur = cur.next

        return hash_map[head]