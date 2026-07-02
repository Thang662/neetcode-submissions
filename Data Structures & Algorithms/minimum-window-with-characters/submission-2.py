from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        matches, l = 0, 0
        cnt_s, cnt_t = defaultdict(int), Counter(t)
        best, best_str = float('inf'), ''

        for r in range(len(s)):
            if s[r] in cnt_t:
                cnt_s[s[r]] += 1

                if cnt_s[s[r]] == cnt_t[s[r]]:
                    matches += 1

            while matches == len(cnt_t):
                if s[l] in cnt_t:
                    cnt_s[s[l]] -= 1

                    if cnt_s[s[l]] + 1 == cnt_t[s[l]]:
                        matches -= 1
                
                if r - l < best:
                    best, best_str = r - l + 1, s[l:r+1]
                l += 1
            
        return best_str
