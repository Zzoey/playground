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
        data = data.encode("utf-8")
        producer.send(self.topic, data)
        producer.flush()

    def Subscriber(self):
        """
        Kafka Subscriber
        """
        print("Listening via Apache Kafka")
        consumer = KafkaConsumer(self.topic, bootstrap_servers=self.bootstrap_servers)
        for message in consumer:
            print(
                "%s:%d:%d: key=%s value=%s"
                % (
                    message.topic,
                    message.partition,
                    message.offset,
                    message.key,
                    message.value,
                )
            )
