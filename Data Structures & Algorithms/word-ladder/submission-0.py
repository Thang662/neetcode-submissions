from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        words, res = set(wordList), 0
        queue = deque([beginWord])

        while queue:
            print(queue)
            res += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    for j in range(97, 123):
                        if chr(j) == word[i]:
                            continue
                        nei = word[:i] + chr(j) + word[i+1:]
                        if nei in words:
                            words.remove(nei)
                            queue.append(nei)

        return 0