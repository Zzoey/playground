from kafka import KafkaProducer, KafkaConsumer
from config import bootstrapserver, topicname


class ApacheKafka:
    def __init__(self, topic=topicname, bootstrap_servers=bootstrapserver):
        self.topic = topic
        self.bootstrap_servers = bootstrap_servers

    def Publisher(self, data):
        """
        Kafka Publisher
        """
        producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers, retries=2)
        producer.send(self.topic, data[0], data[1])
        producer.flush()

    def Subscriber(self):
        """
        Kafka Subscriber
        """
        print("Listening via Apache Kafka")
        consumer = KafkaConsumer(self.topic, bootstrap_servers=self.bootstrap_servers)
        for message in consumer:
            key = message.key.decode() if message.key else None
            return key, message.value
