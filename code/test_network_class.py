from utils.network import SimpleConvNet
from config import device

model = SimpleConvNet()
model.to(device)

print(model)
