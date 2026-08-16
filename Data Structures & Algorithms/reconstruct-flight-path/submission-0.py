from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        res = []
        adj = defaultdict(list)
        for src, des in tickets:
            adj[src].append(des)

        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)
        dfs('JFK')
        return res[::-1]
