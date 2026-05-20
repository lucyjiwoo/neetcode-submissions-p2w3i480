class Twitter:
    def __init__(self):
        self.users = dict()     # user : {follower}
        self.posts = dict()     # user : [time, tweetId]
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.posts:
            self.posts[userId].append([-self.time, tweetId])
        else:
            self.posts[userId] = [[-self.time, tweetId]]
        self.time += 1
    def getNewsFeed(self, userId: int) -> List[int]:
        if not self.posts:
            return []
        feeds = []
        followers = [userId] + list(self.users.get(userId, []))
        for f in followers:
            if f in self.posts:
                feeds = feeds + self.posts[f]
        heapq.heapify(feeds)
        cnt = 0
        res = []
        while feeds and cnt < 10:
            feed = heapq.heappop(feeds)
            res.append(feed[1])
            cnt +=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return 
        if followerId in self.users:
            self.users[followerId].add(followeeId)
        else:
            self.users[followerId] = {followeeId}
        print(self.users)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return 
        self.users[followerId].discard(followeeId)
        print(self.users)
