"""
Python file that contains the network architectures
"""
import torch.nn as nn


class SimpleConvNet(nn.Module):
    def __init__(self):
        super(SimpleConvNet, self).__init__()

        self.layer1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )

        self.layer2 = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.fc1 = nn.Linear(in_features=2304, out_features=1024)
        self.drop = nn.Dropout2d(0.25)
        self.fc2 = nn.Linear(in_features=1024, out_features=100)
        self.fc3 = nn.Linear(in_features=100, out_features=10)

    def forward(self, x):
        out = self.layer1(x)
        # print("1", out.shape)
        out = self.layer2(out)
        # print("2", out.shape)
        # out = self.layer3(out)
        # print("3", out.shape)
        out = out.view(out.size(0), -1)
        # print(out.shape)
        out = self.fc1(out)
        # print("fc1", out.shape)
        out = self.drop(out)
        # print("fc1 drop", out.shape)
        out = self.fc2(out)
        # print("fc2", out.shape)
        out = self.fc3(out)
        # print("fc3", out.shape)

        return out


'''
class Conv_Feat_Extractor(nn.Module):
    """
    Feature extractor for Conv model
    """

    def __init__(self, model_):
        super(Conv_Feat_Extractor, self).__init__()

class Flatten(nn.Module):
    """
    Wrapper class to flatten any tensor.
    """

    def __init__(self):
        super(Flatten, self).__init__()

    def forward(self, x):
        return x.flatten(start_dim=1)
        
'''
