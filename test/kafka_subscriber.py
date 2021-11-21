import sys

sys.path.append("../")
from utils.apache_kafka import ApacheKafka
from config import topicname, bootstrapserver

kafka_obj = ApacheKafka(topicname, bootstrapserver)
kafka_obj.Subscriber()
