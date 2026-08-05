from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacent = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()
        finish = 0
        for a, b in prerequisites:
            adjacent[b].append(a)
            indegree[a] += 1

        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)

        print(indegree, adjacent, queue)
        while queue:
            node = queue.popleft()
            finish += 1
            for i in adjacent[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        return finish == numCourses