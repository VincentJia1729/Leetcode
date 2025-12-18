

class Twitter:

    def __init__(self):
        self.count = 0 # this count will unique across all tweets
        # count will go 0, -1, -2, -3, ...
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetId]
        self.followMap = defaultdict(set) # userId -> set of {followeeId}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:

        res = []
        minHeap = []
        
        self.followMap[userId].add(userId) # apparently the user can see his own tweets
        # he follows himself (weird)
        for followeeId in self.followMap[userId]: # look at the followers of userId
            if followeeId in self.tweetMap: # check to see if this user has tweeted before
               # self.tweetMap, we are checking for keys
               index = len(self.tweetMap[followeeId]) - 1 # get the index of number tweets, tweeted by a particular user
               count, tweetId = self.tweetMap[followeeId][index] # grab the count and tweetId of the most recent tweet of this particular user
               minHeap.append([count, tweetId, followeeId, index - 1]) # notice we only apend a single value to minHeap
               # also notice that we store the index - 1 (the tweet before the most recent one of this particular user)
        heapq.heapify(minHeap) # this heap only has num of elements as users who have tweeted at least once

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap) # pop from minHeap
            res.append(tweetId)
            if index >= 0: # if this particular user has more tweets
                count, tweetId = self.tweetMap[followeeId][index] # notice that this index is already decremented by 1
                # this way we can grab new information in "count" and "tweetId"
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1]) # decrement one more time, to prep for "continued popping"
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)