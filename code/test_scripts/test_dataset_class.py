from torch.utils import data
from utils.dataset import Dataset
from config import train_path, test_path, learning_rate, val_pr, batch_size, transform


training_data = Dataset(
    train_path, learning_rate, val_pr, batch_size, transforms=transform
)

testing_data = Dataset(
    test_path, learning_rate, val_pr, batch_size, transforms=transform
)

if learning_rate == 0:
    dataloaders = testing_data.loadData()
    test_data_loader = dataloaders["val"]
    print(len(test_data_loader))
    print(testing_data.get_text_label(1))
else:
    dataloaders = training_data.loadData()
    train_data_loader = dataloaders["train"]
    val_data_loader = dataloaders["val"]
    print(len(val_data_loader))
    for im, label in val_data_loader:
        sample_image = im[0]  # Reshape them according to your needs.
        sample_label = label[0]
        print(sample_image.shape)
        print(training_data.get_text_label(sample_label))
        break
