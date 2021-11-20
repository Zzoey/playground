import sys

sys.path.append("../")
from apache_kafka import ApacheKafka
from config import topicname, bootstrapserver

kafka_obj = ApacheKafka(topicname, bootstrapserver)
kafka_obj.Publisher("I am Vinay Ch! Yo kafka!!")
