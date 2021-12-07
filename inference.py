import os
import csv
import torch
from PIL import Image
from sklearn.metrics import classification_report, confusion_matrix
from utils.dataset import Dataset
from utils.network import SimpleConvNet

from config import (
    trained_simple_conv_model,
    device,
    test_path,
    val_pr,
    transform,
    batch_size,
    num_classes,
    operate_on_dirs_inference,
)


def get_data():

    test_data_loader = get_dataloader()
    dataloaders = test_data_loader.loadData()
    test_data = dataloaders["val"]
    return test_data


def get_dataloader():

    testing_data_loaders = Dataset(
        test_path,
        0,  # At test time learning rate = 0
        val_pr,
        batch_size,
        transforms=transform,
    )
    return testing_data_loaders


def get_saved_model():
    model = SimpleConvNet()
    model.load_state_dict(torch.load(trained_simple_conv_model, map_location="cpu"))
    model.eval()
    return model


def get_class_names(num_classes):
    data_loader = get_dataloader()
    class_names = []
    for i in range(num_classes):
        class_names.append(data_loader.get_text_label(i))
    return class_names


def get_accuracy(correct, total):
    accuracy = correct * 100 / total
    return accuracy.detach().cpu().numpy()


def get_classification_report(gt, predictions, class_names):

    _report = classification_report(
        gt,
        predictions,
        target_names=class_names,
        labels=range(len(class_names)),
    )
    return _report


def get_confusion_matrix(gt, predictions):
    cm = confusion_matrix(gt, predictions)
    return cm


def inference_on_set_of_images(input_path, output_path):

    model = get_saved_model()
    data_loader = get_dataloader()
    image_list = [
        f for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f))
    ]
    with open(os.path.join(output_path, "output.csv"), mode="w") as out:
        out_writer = csv.writer(
            out, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        for img in image_list:
            image = Image.open(os.path.join(input_path, img)).convert("RGB")
            image = transform(image)
            image = image.to(device)
            image.unsqueeze_(0)
            image_out = model(image)
            predicted_label = torch.argmax(image_out).item()
            class_label = data_loader.get_text_label(predicted_label)
            out_writer.writerow([img, class_label])
            # print(img, class_label)
    print(
        "Inference completed on set of {} images and output.csv is generated".format(
            len(image_list)
        )
    )


def main():

    total_predictions, total_gt = [], []
    correct, total = 0, 0

    test_data = get_data()
    model = get_saved_model()
    class_names = get_class_names(num_classes)

    for images, labels in test_data:
        images = images.to(device)
        output = model(images)
        _, predictions = torch.max(output, 1)
        total_predictions.extend(predictions.detach().cpu().numpy())
        total_gt.extend(labels)
        correct += (predictions == labels).sum()
        total += len(labels)

    classfication_report_ = get_classification_report(
        total_gt, total_predictions, class_names
    )
    confusion_matrix_ = get_confusion_matrix(
        total_gt,
        total_predictions,
    )

    print(classfication_report_)
    # print(confusion_matrix_)


if __name__ == "__main__":
    operate_on_dirs_inference()
    main()  # runs inference on the test set of the FashionMNIST
    # inference_on_set_of_images(input_path, output_path)  # run inference on set of images from a folder
