from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)
        queue = deque([(0, -1)])
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        while queue:
            node, parent = queue.popleft()
            visited.add(node)

            for i in adj[node]:
                if i == parent:
                    continue
                elif i not in visited:
                    queue.append((i, node))
                else:
                    return False
        return len(visited) == n