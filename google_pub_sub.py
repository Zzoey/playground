import os
from config import key_path, topic_path, subscription_path
from google.cloud import pubsub_v1


class GcpPubSub:
    def __init__(self, topic=topic_path, path=key_path, subscription=subscription_path):
        self.topic = topic
        self.path = path
        self.subscription = subscription

    def authenticate(self):
        """
        Pub/Sub Authenticator
        """
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.path

    def Publisher(self, data="I am Vinay"):
        """
        Pub/Sub Publisher
        """
        self.authenticate()
        publisher = pubsub_v1.PublisherClient()
        data = data.encode("utf-8")
        attributes = {"name": "Vinay", "age": "26"}
        future = publisher.publish(self.topic, data, **attributes)
        print(f"published message id: {future.result()}")

    def Subscriber(self, timeout=5.0):
        """
        Pub/Sub Subscriber
        """
        self.authenticate()
        print("Listening via Google Pub Sub")
        subscriber = pubsub_v1.SubscriberClient()

        def callback(message):
            print(f"Received the note: {message}")
            if message.attributes:
                print("Attributes:")
                for key in message.attributes:
                    value = message.attributes.get(key)
                    print(f"{key}: {value}")

            message.ack()

        future = subscriber.subscribe(self.subscription, callback=callback)
        # print(f"Listening for messages on {self.subscription}")

        with subscriber:
            try:
                # future.result(timeout=timeout)
                future.result()  # without timeout it will be indefinite
            except TimeoutError:
                future.cancel()
                future.result()
