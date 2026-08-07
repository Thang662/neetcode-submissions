from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node: int, parent: int) -> bool:
            if node in visited:
                return False

            visited.add(node)

            for i in adj[node]:
                if i == parent:
                    continue
                if not dfs(i, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n