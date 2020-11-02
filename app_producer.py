from dataclasses import dataclass, field
import json
import random

from confluent_kafka import Consumer, Producer
from confluent_kafka.admin import AdminClient, NewTopic
from faker import Faker
from datetime import datetime


faker = Faker()

BROKER_URL = "PLAINTEXT://localhost:29092"
TOPIC_NAME = "org.waelson.app.purchases"


@dataclass
class Purchase:
    username: str = field(default_factory=faker.user_name)
    currency: str = field(default_factory=faker.currency_code)
    amount: int = field(default_factory=lambda: random.randint(100, 200000))

    def serialize(self):
        """Serializes the object in JSON string format"""
        # TODO: Serializer the Purchase object
        #       See: https://docs.python.org/3/library/json.html#json.dumps
        return json.dumps(
            {
                "username": self.username,
                "currency": self.currency,
                "amount": self.amount,
            }
        )


def produce_sync_async(topic_name):
    """Produces data synchronously into the Kafka Topic"""
    p = Producer({"bootstrap.servers": BROKER_URL})

    # TODO: Write a synchronous production loop.
    #       See: https://docs.confluent.io/current/clients/confluent-kafka-python/#confluent_kafka.Producer.flush

    start_time = datetime.utcnow()
    curr_interaction = 1
    while True:
        # TODO: Instantiate a `Purchase` on every iteration. Make sure to serialize it before
        #       sending it to Kafka!
        content = Purchase().serialize()
        #print(f"{curr_interaction}: Sending message {content}")

        p.produce(topic_name, content)

        # p.flush()  # <=== This command is what do a producer to be sync. It makes the producer
        #      to wait for a server response. You can to uncomment this command to send asyn messages.

        if curr_interaction % 1000 == 0:
            elapsed = (datetime.utcnow() - start_time).seconds
            print(
                f"Messages sent: {curr_interaction} | Total elapsed seconds: {elapsed}")
            start_time = datetime.utcnow()
        curr_interaction = 1 + curr_interaction


def main():
    print(f"Starting application")
    """Checks for topic and creates the topic if it does not exist"""
    print(
        f"Checks for topic and creates the topic if it does not exist '{TOPIC_NAME}''")
    create_topic(TOPIC_NAME)
    try:
        produce_sync_async(TOPIC_NAME)
    except KeyboardInterrupt as e:
        print("shutting down")


def create_topic(client):
    """Creates the topic with the given topic name"""
    client = AdminClient({"bootstrap.servers": BROKER_URL})
    futures = client.create_topics(
        [NewTopic(topic=TOPIC_NAME, num_partitions=5, replication_factor=1)]
    )
    for _, future in futures.items():
        try:
            future.result()
        except Exception as e:
            pass


if __name__ == "__main__":
    main()
