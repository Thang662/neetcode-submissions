from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        counts = Counter(tasks)
        
        heap = [-count for count in counts.values()]
        cooldown = deque()
        heapq.heapify(heap)

        while heap or cooldown:
            time += 1

            if heap:
                cnt = heapq.heappop(heap)
                cnt += 1

                if cnt != 0:
                    cooldown.append((time + n, cnt))

            if cooldown and cooldown[0][0] == time:
                _, cnt  = cooldown.popleft()
                heapq.heappush(heap, cnt)

        return time

        