from flask import json
from .config import RABBITMQ_HOST, RABBITMQ_QUEUE
import pika


def publish_to_matching_queue(message):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=RABBITMQ_HOST)
        )
        channel = connection.channel()

        channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)

        channel.basic_publish(
            exchange="",
            routing_key=RABBITMQ_QUEUE,
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
        )
        connection.close()
    except pika.exceptions.AMQPConnectionError:
        return {"error": "Failed to connect to RabbitMQ. Please try again later."}, 500

    except pika.exceptions.ChannelError:
        return {"error": "RabbitMQ channel error. Please try again later."}, 500

    except Exception as e:
        return {"error": f"An unexpected error occurred with RabbitMQ."}, 500
