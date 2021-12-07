import json
from unified_api import UnifiedApi
from config import api_name

api_name = "kafka"
topic_name = "results"

u_api = UnifiedApi()
result_object = u_api.selectApi(api_name, topic_name)

while 1:
    (key, value) = result_object.Subscriber()
    true_val = json.loads(value)
    print("Predicted Label:", true_val)
