from .celery import app
import time
import redis

r = redis.Redis(host="redis", port=6379, db=0)


from .celery import app


@app.task(
    name="process_match",
    queue="matching_queue",
    bind=True,
    max_retries=3,
)
def process_matching_request(self, user_data):
    user_id = user_data["user_id"]
    topic = user_data["topic"]
    difficulty = user_data["difficulty"]
    print(
        f"Processing request for user: {user_id}, topic: {topic}, difficulty: {difficulty}"
    )

    # current_time = time.time()
    # min_timestamp = current_time - 30
    # key = f"matching:{topic}:{difficulty}"
    # r.zremrangebyscore(key, "-inf", min_timestamp)

    # complete_matches = r.zrangebyscore(key, min_timestamp, "+inf")
    # if len(complete_matches) > 0:
    #     match = complete_matches[0]
    #     r.zrem(key, match)
    #     print(f"complete matched with: {match.decode('utf-8')}")
    #     return
    # r.zadd(key, {str(user_data): current_time})

    # topic_key = f"matching:{topic}"
    # topic_matches = r.zrangebyscore(key, min_timestamp, "+inf")
    # if len(topic_matches) > 0:
    #     match = topic_matches[0]
    #     r.zrem(key, match)
    #     print(f"parital matched with: {match.decode('utf-8')}")
    #     return

    # r.zadd(topic_key, {str(user_data): current_time})
