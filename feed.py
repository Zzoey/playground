import torch
import io
from utils.dataset import Dataset
from unified_api import UnifiedApi

from config import test_path, val_pr, transform, api_name


def get_data(test_data_loader):
    dataloaders = test_data_loader.loadData()
    test_data = dataloaders["val"]
    return test_data


def get_dataloader():

    testing_data_loaders = Dataset(
        test_path,
        0,  # At test time learning rate = 0
        val_pr,
        1,  # get all images in one batch
        transforms=transform,
    )
    return testing_data_loaders


# select the unified API
u_api = UnifiedApi()
messenger_object = u_api.selectApi(api_name)
test_data_loader = get_dataloader()
test_data = get_data(test_data_loader)

print("Feeding test set!")

for i, img in enumerate(test_data):
    (img, label) = img[0], img[1]
    text_label = test_data_loader.get_text_label(label)
    with io.BytesIO() as buff:
        buff = io.BytesIO()
        torch.save(img, buff)
        buff.seek(0)
        key = f"image-{i}-with-label-{text_label}"
        messenger_object.Publisher((buff.getvalue(), key.encode()))
        print(f"Pushed an Image labelled {text_label}")
    q = input("Press q to exit")
    if q == "q":
        exit(0)
