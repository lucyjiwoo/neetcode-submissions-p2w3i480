class Twitter:

    def __init__(self):
        self.time = 0               # bigger time means older post
        self.tweets = dict()        # key(userId): [time, tweets that this user posted]
        self.follows = dict()        # userId: following userId dict
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId] = self.tweets.get(userId,[])+[[self.time,tweetId]]
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        followings = self.follows.get(userId, [])
        if followings:
            followings = followings.keys()
        pq = list(self.tweets.get(userId, [])) 
        for f in followings:
            pq += self.tweets.get(f, [])
        heapq.heapify(pq)
        res,c  = [], 0
        while c < 10 and pq:
            v = heapq.heappop(pq)
            if v[1] not in res:
                res.append(v[1])
            c +=1
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId] = self.follows.get(followerId, dict())
        self.follows[followerId][followeeId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId] = self.follows.get(followerId, dict())
        if followeeId in self.follows[followerId]:
            self.follows[followerId].pop(followeeId)
