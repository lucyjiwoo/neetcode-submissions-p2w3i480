class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = dict()      # userId -> [[time, tweetId], ...]
        self.follows = dict()     # userId -> {followeeId: True}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId] = self.tweets.get(userId, []) + [[self.time, tweetId]]
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followings = self.follows.get(userId, {})
        pq = list(self.tweets.get(userId, []))

        for f in followings:
            pq += self.tweets.get(f, [])

        heapq.heapify(pq)

        res = []
        while len(res) < 10 and pq:
            time, tweetId = heapq.heappop(pq)
            res.append(tweetId)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        
        if followerId == followeeId:
            return
        self.follows[followerId] = self.follows.get(followerId, {})
        self.follows[followerId][followeeId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId] = self.follows.get(followerId, {})
        if followeeId in self.follows[followerId]:
            self.follows[followerId].pop(followeeId)