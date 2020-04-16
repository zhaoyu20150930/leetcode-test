from typing import List

"""
设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

postTweet(userId, tweetId): 创建一条新的推文
getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
follow(followerId, followeeId): 关注一个用户
unfollow(followerId, followeeId): 取消关注一个用户
示例:

Twitter twitter = new Twitter();

// 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
twitter.postTweet(1, 5);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
twitter.getNewsFeed(1);

// 用户1关注了用户2.
twitter.follow(1, 2);

// 用户2发送了一个新推文 (推文id = 6).
twitter.postTweet(2, 6);

// 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
// 推文id6应当在推文id5之前，因为它是在5之后发送的.
twitter.getNewsFeed(1);

// 用户1取消关注了用户2.
twitter.unfollow(1, 2);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
// 因为用户1已经不再关注用户2.
twitter.getNewsFeed(1);

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-twitter
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Twitter:

    def __init__(self):
        import time
        self.t = time
        self.ut = {}  # 用户twitter
        self.uf = {}  # 用户follow

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.ut:
            self.ut[userId].append((tweetId, self.t.time()))
        else:
            self.ut[userId] = [(tweetId, self.t.time())]

    def getNewsFeed(self, userId: int) -> List[int]:
        myt = []
        if userId in self.ut:
            myt = self.ut[userId][:-11:-1]
        if userId in self.uf:
            for f in self.uf[userId]:
                if f in self.ut:
                    myt.extend(self.ut[f][:-11:-1])
        myt.sort(key=lambda x: x[1])
        return [i[0] for i in myt[:-11:-1]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            if followerId in self.uf:
                self.uf[followerId].add(followeeId)
            else:
                self.uf[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.uf:
            if followeeId in self.uf[followerId]:
                self.uf[followerId].remove(followeeId)


if __name__ == '__main__':
    obj = Twitter()
    obj.postTweet(1, 5)
    assert obj.getNewsFeed(1) == [5]
    obj.follow(1, 2)
    obj.postTweet(2, 6)
    assert obj.getNewsFeed(1) == [6, 5]
    obj.unfollow(1, 2)
    assert obj.getNewsFeed(1) == [5]
