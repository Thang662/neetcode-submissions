class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        checked = [False for i in range(len(nums))]
        res = []

        def dfs(path: list[int], check: list[bool]) -> None:
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if check[i]:
                    continue
                check[i] = True
                path.append(nums[i])
                dfs(path, check)
                check[i] = False
                path.pop()
                
        dfs([], checked)
        return res