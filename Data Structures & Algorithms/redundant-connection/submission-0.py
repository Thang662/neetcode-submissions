from collections import defaultdict, deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        queue = deque()
        adj = defaultdict(list)
        indegree = defaultdict(int)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
            
        for i in range(1, len(edges)+1):
            if indegree[i] == 1:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            indegree[node] -= 1
            for i in adj[node]:
                indegree[i] -= 1
                if indegree[i] == 1:
                    queue.append(i)
                    
        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v]:
                return [u, v]
        return []
