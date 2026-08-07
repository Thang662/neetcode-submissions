from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = defaultdict(list)
        res = 0
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node: int, parent: int) -> None:
            if node in visited:
                return

            visited.add(node)
            for i in adj[node]:
                if i == parent:
                    continue
                dfs(i, node)

        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                res += 1

        return res