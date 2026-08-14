import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        edges = defaultdict(list)

        for u, v, price in flights:
            edges[u].append((v, price))

        # (total_cost, edges_used, node)
        heap = [(0, 0, src)]

        # best[(node, edges_used)] = minimum cost
        best = {(src, 0): 0}

        while heap:
            cost, edges_used, node = heapq.heappop(heap)

            if node == dst:
                return cost

            # k stops means at most k + 1 flights
            if edges_used == k + 1:
                continue

            for nei, price in edges[node]:
                new_cost = cost + price
                new_edges = edges_used + 1

                if (
                    (nei, new_edges) not in best
                    or new_cost < best[(nei, new_edges)]
                ):
                    best[(nei, new_edges)] = new_cost
                    heapq.heappush(
                        heap,
                        (new_cost, new_edges, nei)
                    )

        return -1