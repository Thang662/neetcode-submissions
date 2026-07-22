from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = {userId} | self.follows[userId]
        heap = []

        for user in users:
            for post in self.posts[user]:
                heapq.heappush(heap, (-post[1], post[0]))

        res = []
        
        while heap and len(res) < 10:
            res.append(heapq.heappop(heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
