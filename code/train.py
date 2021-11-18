import torch
import torch.nn as nn
from utils.dataset import Dataset
from utils.network import SimpleConvNet
from utils.trainer import Trainer

from config import *


def get_model(device=device):
    model = SimpleConvNet()
    model = model.to(device)
    return model


def get_loss_type():
    if loss_type == "mse":
        criterion = nn.MSELoss().to(device)
    elif loss_type == "mae":
        criterion = nn.MAELoss().to(device)
    else:
        criterion = nn.CrossEntropyLoss().to(device)
    return criterion


def main():
    model = get_model()
    training_data_loaders = Dataset(
        train_path, learning_rate, val_pr, batch_size, transforms=transform
    )
    dataloaders = training_data_loaders.loadData()
    train_data = dataloaders["train"]
    val_data = dataloaders["val"]

    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    criterion = get_loss_type()
    trainer = Trainer(criterion, model, device, epochs, train_data, val_data, optimizer)
    trainer.train()


if __name__ == "__main__":
    # operate_on_dirs_training()
    main()
