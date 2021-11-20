import sys

sys.path.append("../")
from google_pub_sub import GcpPubSub
from config import key_path, topic_path, subscription_path

pub_sub_obj = GcpPubSub(topic_path, key_path, subscription_path)
pub_sub_obj.Publisher("I am Vinay Ch")
