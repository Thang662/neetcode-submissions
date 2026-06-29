class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l = 0, 0
        last = {}

        # variable window size using pointer + hash map
        # time: O(n) space: O(n)
        for i in range(len(s)):
            if s[i] in last:
                l = max(last[s[i]] + 1, l)
            last[s[i]] = i
            res = max(res, i - l + 1)
            
        return res