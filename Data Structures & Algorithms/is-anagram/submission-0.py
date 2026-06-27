class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        freqs = {}
        for c in s:
            freqs[c] = freqs.get(c, 0) + 1

        for c in t:
            freqs[c] = freqs.get(c, 0) - 1
            if freqs[c] < 0:
                return False

        return True
        