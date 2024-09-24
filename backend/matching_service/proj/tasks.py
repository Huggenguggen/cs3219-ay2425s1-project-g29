from .celery import app
import time
import redis

# Initialize Redis client
r = redis.Redis(host="redis", port=6379, db=0)


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

    while time.time() < current_time + 30:
        try:
            r.zremrangebyscore(key, "-inf", min_timestamp)
            r.zremrangebyscore(topic_key, "-inf", min_timestamp)

            r.watch(key)
            pipe = r.pipeline()
            pipe.multi()

            complete_matches = r.zrangebyscore(key, min_timestamp, "+inf")
            if complete_matches:
                match = complete_matches[0]
                pipe.zrem(key, match)
                pipe.execute()

                print(
                    f"Complete match found: user_id={user_id}, matched_with={match.decode('utf-8')}"
                )
                return

            pipe.zadd(key, {str(user_data): current_time})
            pipe.execute()
            print(
                f"Added user_id={user_id} to matching set for topic={topic} and difficulty={difficulty}"
            )

            r.watch(topic_key)
            pipe = r.pipeline()
            pipe.multi()

            topic_matches = r.zrangebyscore(topic_key, min_timestamp, "+inf")
            if topic_matches:
                match = topic_matches[0]
                pipe.zrem(topic_key, match)
                pipe.execute()

                print(
                    f"Partial match found: user_id={user_id}, matched_with={match.decode('utf-8')}"
                )
                return

            pipe.zadd(topic_key, {str(user_data): current_time})
            pipe.execute()
            print(
                f"No match found for user_id={user_id}, added to topic matching queue: {topic_key}"
            )

        except redis.WatchError:
            print("Transaction failed due to concurrent modification, retrying...")

        finally:
            pipe.reset()
