import redis
import datetime


ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432

def article_vote(redis, user, article):
	#2018-04-11 01:23:59.118211 - 7 days, 0:00:00
    cutoff = datetime.datetime.now() - datetime.timedelta(seconds=ONE_WEEK_IN_SECONDS)
    # print(cutoff)
    # 
    if not datetime.datetime.fromtimestamp(redis.zscore('time:', article)) < cutoff:
        article_id = article.split(':')[-1]
<<<<<<< HEAD
        if redis.sadd('voted:' + article_id, user):
            redis.zincrby(name='score:', value=article, amount=VOTE_SCORE)
            redis.hincrby(name=article, key='votes', amount=1)
=======
        
        if redis.sadd('voted:' + article_id, user):
            redis.zincrby('score:', VOTE_SCORE, article)
            reids.hincrby(article, 'votes', 1)
        # print(artical_id)
   
>>>>>>> homework-2

def article_switch_vote(redis, user, from_article, to_article):
    # HOMEWORK 2 Part I 
    from_article_id = from_article.split(':')[-1]
    to_article_id = to_article.split(':')[-1]

    redis.srem('voted:' + from_article_id, user)
    redis.sadd('voted:' + to_article_id, user)
    # or redis.smove('voted:' + from_article_id, 'voted:' + to_article_id, user)
    

    from_article_score = redis.zscore('score:', 'article:'+ from_article_id)
    changed_from_article_score = from_article_score - 432
    to_article_score = redis.zscore('score:', 'article:'+ to_article_id)
    changed_to_article_score = to_article_score + 432

    redis.zrem('score:', 'article:'+ from_article_id)
    redis.zadd('score:', changed_from_article_score, 'article:'+ from_article_id)
    redis.zrem('score:', 'article:'+ to_article_id)
    redis.zadd('score:', changed_to_article_score, 'article:'+ to_article_id)

    
	# redis.zincrby('score:', -432, 'article:'+ from_article_id)

redis = redis.StrictRedis(host='localhost', port=6379, db=0)

# user:3 up votes article:1
article_vote(redis, "user:3", "article:1")

# user:3 up votes article:3
article_vote(redis, "user:3", "article:3")
<<<<<<< HEAD
=======

>>>>>>> homework-2
# user:2 switches their vote from article:8 to article:1
article_switch_vote(redis, "user:2", "article:8", "article:1")


# Which article's score is between 10 and 20?
# PRINT THE ARTICLE'S LINK TO STDOUT:
# HOMEWORK 2 Part II
article = redis.zrangebyscore("score:", 10, 20) 
print(article)
print(redis.hget("article:8", "link"))






