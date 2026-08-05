from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacent = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()
        visited = set()
        for a, b in prerequisites:
            adjacent[a].append(b)
            indegree[b] += 1

        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)

        while queue:
            node = queue.popleft()
            visited.add(node)
            for i in adjacent[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    # if i 
                    queue.append(i)
        return len(visited) == numCourses