import io
import json
import torch
from utils.network import SimpleConvNet
from unified_api import UnifiedApi
from utils.dataset import Dataset

from config import (
    trained_simple_conv_model,
    device,
    test_path,
    val_pr,
    transform,
    api_name,
)


def get_dataloader():

    testing_data_loaders = Dataset(
        test_path,
        0,  # At test time learning rate = 0
        val_pr,
        1,  # get all images in one batch
        transforms=transform,
    )
    return testing_data_loaders


def get_saved_model():
    model = SimpleConvNet()
    model.load_state_dict(torch.load(trained_simple_conv_model, map_location="cpu"))
    model.eval()
    return model


def prediction(value, model):
    image = torch.load(io.BytesIO(value))
    image = image.to(device)
    image.unsqueeze(0)
    image_out = model(image)
    predicted_label = torch.argmax(image_out).item()
    class_label = get_dataloader().get_text_label(predicted_label)
    return class_label, image.shape


u_api = UnifiedApi()
messenger_object = u_api.selectApi(api_name)

topic_name = "results"
result_object = u_api.selectApi(api_name, topic_name)
model = get_saved_model()

while 1:
    (key, value) = messenger_object.Subscriber()
    class_label, shape = prediction(value, model)

    print(f"Received an image with key {key}, It is now classified and being pushed.")
    result_object.Publisher((json.dumps(class_label).encode(), key.encode()))
