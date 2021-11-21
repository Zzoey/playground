from config import *
from utils.apache_kafka import ApacheKafka
from utils.google_pub_sub import GcpPubSub


class UnifiedApi:
    def selectApi(self, _api_name):
        if _api_name == "pubsub":
            pub_sub_obj = GcpPubSub(topic_path, key_path, subscription_path)
            return pub_sub_obj
        elif _api_name == "kafka":
            kafka_obj = ApacheKafka(topicname, bootstrapserver)
            return kafka_obj
        else:
            print("Select 'pubsub' or 'kafka'")
