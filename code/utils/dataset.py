import torch
from torchvision import datasets
from torch.utils.data import random_split


class Dataset:
    """
    Class for images loading / transforming
    Arguments:
        - path: path to the image folder
        - transforms: transformation to apply
        - ext: .jpg or .png
    """

    def __init__(
        self,
        path,
        learning_rate,
        val_pr,
        batch_size,
        transforms=None,
        device=None,
        ext=".png",
    ):
        self.path = path
        self.learning_rate = learning_rate
        self.val_pr = val_pr
        self.ext = ext
        self.batch_size = batch_size
        self.transforms = transforms
        self.device = device

    def loadData(self):

        image_dataset = datasets.ImageFolder(self.path, transform=self.transforms)
        total_images = len(image_dataset)
        self._dataloaders = {}

        if self.learning_rate == 0:

            self._dataloaders["val"] = torch.utils.data.DataLoader(
                image_dataset,
                batch_size=self.batch_size,
                shuffle=True,
                num_workers=4,
            )

        else:

            split = self.val_pr
            train_images = int(len(image_dataset) * (1 - split))
            val_images = int(len(image_dataset) * split)

            train_data, val_data = random_split(
                image_dataset,
                [train_images, val_images],
                generator=torch.Generator().manual_seed(42),
            )

            self._dataloaders["train"] = torch.utils.data.DataLoader(
                train_data,
                batch_size=self.batch_size,
                shuffle=True,
                num_workers=4,
            )
            self._dataloaders["val"] = torch.utils.data.DataLoader(
                val_data,
                batch_size=self.batch_size,
                shuffle=True,
                num_workers=4,
            )

        self.class_names = image_dataset.classes
        # print(f"Classes: {self.class_names}")
        return self._dataloaders

    def get_text_label(self, label):
        output_mapping = {
            0: "T-shirt/Top",
            1: "Trouser",
            2: "Pullover",
            3: "Dress",
            4: "Coat",
            5: "Sandal",
            6: "Shirt",
            7: "Sneaker",
            8: "Bag",
            9: "Ankle Boot",
        }
        input = label.item() if type(label) == torch.Tensor else label
        return output_mapping[input]
