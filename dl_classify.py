import io
import json
import torch
from utils.network import SimpleConvNet
from unified_api import UnifiedApi
from feed import get_dataloader

from config import trained_simple_conv_model, device


api_name = "kafka"


def get_saved_model():
    model = SimpleConvNet()
    model.load_state_dict(torch.load(trained_simple_conv_model, map_location="cpu"))
    model.eval()
    return model


def prediction(key, value, model):
    image = torch.load(io.BytesIO(value))
    image = image.to(device)
    image.unsqueeze_(0)
    image_out = model(image)
    predicted_label = torch.argmax(image_out).item()
    class_label = get_dataloader().get_text_label(predicted_label)
    return class_label


u_api = UnifiedApi()
messenger_object = u_api.selectApi(api_name)
model = get_saved_model()

messenger_object.Subscriber()  # TODO: this should return key, value & implement return in Kafka client
# print(f"Received an {image.shape} with key {key}, It is now classified and pushed.")

class_label = prediction(key, value, model)
messenger_object.Publisher(json.dumps(class_label).encode(), key=key.encode())
