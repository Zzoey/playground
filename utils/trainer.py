"""
Python file for trainer
"""
import torch
import os
import random
from config import model_path  # , training_models

random.seed(0)


class Trainer:
    """
    Wrapper class for training
    Parameters:
        - criteron : criterion used for training
        - model : model
        - device : torch.device instance
        - epochs: # epochs used for the training
        - data_loader : DataLoader object that contains the training data
        - data_loader_val: DataLoader object that contains the val data
        - optimizer : torch.optim object
    """

    def __init__(
        self,
        criterion,
        model,
        device,
        epochs,
        data_loader,
        data_loader_val,
        optimizer,
    ):
        self.criterion = criterion
        self.device = device
        self.model = model.to(self.device)
        self.epochs = epochs
        self.data_loader = data_loader
        self.data_loader_val = data_loader_val
        self.optimizer = optimizer
        self.path_model = os.path.join(
            model_path,  # training_models
            "{}.p".format(
                (self.model.__class__.__name__)
                + "_"
                + (self.criterion.__class__.__name__)
                + "_"
                + str(epochs)
                + "_"
                + "epochs"
            ),
        )

    def train(self):
        """
        Function to train and evalutate the model on the val data. The best model on the val set is saved
        """
        best_val_loss = 2
        for e in range(self.epochs):
            self.model = self.model.train()
            running_loss = 0
            i = 0
            for x_batch, labels in self.data_loader:

                self.optimizer.zero_grad()
                x_batch = x_batch.to(self.device)

                out_batch = self.model(x_batch)
                loss = self.criterion(out_batch, labels)
                loss.backward()
                # print(loss)
                self.optimizer.step()
                running_loss += loss.item()
                i += 1
                if i % 10 == 0:
                    print("Loss : {}".format(running_loss / 10))
                    running_loss = 0
                    # break
            best_val_loss = self.eval_and_save(best_val_loss, e)

    def eval_and_save(self, best_loss, e):
        self.model = self.model.eval()
        running_loss = 0
        le = 0
        for x_batch, labels in self.data_loader_val:
            x_batch = x_batch.to(self.device)
            le += x_batch.shape[0]
            out_batch = self.model(x_batch)
            running_loss += self.criterion(out_batch, labels).item()
        running_loss /= le
        print("Epoch: {} \tValidation Loss: {:.6f}".format(e + 1, running_loss))

        if running_loss < best_loss:
            best_loss = running_loss
            torch.save(self.model.state_dict(), self.path_model)
        return best_loss
