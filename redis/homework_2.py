import redis
import datetime


ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432

def article_vote(redis, user, article):
	#2018-04-11 01:23:59.118211 - 7 days, 0:00:00
    cutoff = datetime.datetime.now() - datetime.timedelta(seconds=ONE_WEEK_IN_SECONDS)
	
    print(cutoff)
    if not datetime.datetime.fromtimestamp(redis.zscore('time:', article)) < cutoff:
        article_id = article.split(':')[-1]
        
        if redis.sadd('voted:' + article_id, user):
            redis.zincrby('score:', VOTE_SCORE, article)
            reids.hincrby(article, 'votes', 1)
        # print(artical_id)
   

def article_switch_vote(redis, user, from_article, to_article):
    # HOMEWORK 2 Part I 
    from_article_id = from_article.split(':')[-1]
    to_article_id = to_article.split(':')[-1]

    redis.srem('voted:' + from_article_id, user)
    redis.sadd('voted:' + to_article_id, user)
    

redis = redis.StrictRedis(host='localhost', port=6379, db=0)

# user:3 up votes article:1
article_vote(redis, "user:3", "article:1")
# print(article_vote(redis, "user:3", "article:1"))

# user:3 up votes article:3
article_vote(redis, "user:3", "article:3")
print(article_vote(redis, "user:3", "article:3"))

# user:2 switches their vote from article:8 to article:1
article_switch_vote(redis, "user:2", "article:8", "article:1")
a = "article:8"
b = a.split(':')[-1]
print(b)

# Which article's score is between 10 and 20?
# PRINT THE ARTICLE'S LINK TO STDOUT:
# HOMEWORK 2 Part II
article = redis.zrangebyscore("score:", 10, 20) 
print(redis.hget(article, "link"))

