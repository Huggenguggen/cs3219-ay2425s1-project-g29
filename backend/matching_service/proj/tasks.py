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
        f"Received matching request: user_id={user_id}, topic={topic}, difficulty={difficulty}"
    )

    current_time = time.time()
    min_timestamp = current_time - 30
    key = f"matching:{topic}:{difficulty}"
    topic_key = f"matching:{topic}"
    r.zremrangebyscore(key, "-inf", min_timestamp)
    r.zremrangebyscore(topic_key, "-inf", min_timestamp)

    complete_matches = r.zrangebyscore(key, min_timestamp, "+inf")
    if len(complete_matches) > 0:
        match = complete_matches[0]
        r.zrem(key, match)
        print(
            f"Complete match found: user_id={user_id}, matched_with={match.decode('utf-8')}"
        )
        return

    r.zadd(key, {str(user_data): current_time})
    print(
        f"Added user_id={user_id} to matching set for topic={topic} and difficulty={difficulty}"
    )
    topic_matches = r.zrangebyscore(topic_key, min_timestamp, "+inf")
    if len(topic_matches) > 0:
        match = topic_matches[0]
        r.zrem(topic_key, match)
        print(
            f"Partial match found: user_id={user_id}, matched_with={match.decode('utf-8')}"
        )
        return
    r.zadd(topic_key, {str(user_data): current_time})
    print(
        f"No match found for user_id={user_id}, added to topic matching queue: {topic_key}"
    )
