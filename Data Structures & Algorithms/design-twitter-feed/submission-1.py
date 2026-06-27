from collections import defaultdict
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        print(self.tweets, self.follows)        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        result = []

        # User should always see their own tweets
        users = self.follows[userId] | {userId}

        for uid in users:
            if self.tweets[uid]:
                index = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][index]

                # max heap using negative time
                heapq.heappush(heap, (-time, tweetId, uid, index))

        while heap and len(result) < 10:
            neg_time, tweetId, uid, index = heapq.heappop(heap)
            result.append(tweetId)

            # Move to the previous tweet from the same user
            if index > 0:
                next_index = index - 1
                time, next_tweetId = self.tweets[uid][next_index]
                heapq.heappush(heap, (-time, next_tweetId, uid, next_index))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
