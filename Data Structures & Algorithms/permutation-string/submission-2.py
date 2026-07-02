class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        cnt_s1, cnt_s2 = [0] * 26, [0] * 26
        l = 0
        matches = 0

        for i in range(len(s1)):
            cnt_s1[ord(s1[i]) - ord('a')] += 1
            cnt_s2[ord(s2[i]) - ord('a')] += 1

        matches = sum([1 for i in range(26) if cnt_s1[i] == cnt_s2[i]])
        if matches == 26:
            return True
        
        for r in range(len(s1), len(s2)):
            index = ord(s2[r]) - ord('a')
            cnt_s2[index] += 1
            if cnt_s2[index] == cnt_s1[index]:
                matches += 1
            elif cnt_s2[index] - 1 == cnt_s1[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            cnt_s2[index] -= 1
            if cnt_s2[index] == cnt_s1[index]:
                matches += 1
            elif cnt_s2[index] + 1  == cnt_s1[index]:
                matches -= 1

            l += 1

            if matches == 26:
                return True

        return False