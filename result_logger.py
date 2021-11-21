import json
from unified_api import UnifiedApi

api_name = "kafka"

u_api = UnifiedApi()
messenger_object = u_api.selectApi(api_name)
value, key = messenger_object.Subscriber()  # TODO: this should return prediction,
true_val = json.loads(value)

print("Printing what is received...")
print(key, true_val)
