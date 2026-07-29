from collections import defaultdict, deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return 
        node2node = defaultdict(Node)
        queue = deque([node])
        
        while queue:
            cur_node = queue.popleft()

            node2node[cur_node].val = cur_node.val

            if cur_node.neighbors:
                for neighbor in cur_node.neighbors:
                    if neighbor not in node2node:
                        queue.append(neighbor)
                    node2node[cur_node].neighbors.append(node2node[neighbor])

        return node2node[node]