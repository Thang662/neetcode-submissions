class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res_0, res_1 = 0, 0

        for i in range(len(cost)-1):
            res_0, res_1 = res_1, min(res_0 + cost[i], res_1 + cost[i+1])
            print(res_0, res_1)

        return res_1 