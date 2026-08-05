from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()
        res = []
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        # def find_topo_sort() -> None:
        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)
        print(queue)
        while queue:
            node = queue.popleft()
            res.append(node)
            for i in adj[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        return res if len(res) == numCourses else []