from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freqs = defaultdict(int)
        max_freq = 0
        res = 0

        # Variable window size using pointers
        """
        The variable maxf tracks the highest frequency seen while expanding the window, not 
        necessarily the exact maximum frequency after every shrink. A common mistake is 
        recalculating the maximum by iterating through all counts after moving the left pointer.
        In the optimal solution, you do not need to decrease maxf when shrinking. A stale, higher 
        maxf can temporarily make the validity check more permissive and allow an actually invalid 
        current window, but it does not affect correctness because it cannot make the algorithm 
        record a length larger than one that was achievable when maxf was accurate.
        """
        for r in range(len(s)):
            freqs[s[r]] += 1
            max_freq = max(max_freq, freqs[s[r]])

            while r - l + 1 - max_freq > k:
                freqs[s[l]] -= 1
                l += 1
            print(l, r, max_freq, freqs)
            res = max(res, r - l + 1)

        return res