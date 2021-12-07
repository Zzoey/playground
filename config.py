import os
import torch
import torchvision.transforms as transforms
import shutil


def get_device(gpu_number):
    if torch.cuda.is_available():
        device = torch.device("cuda:{}".format(gpu_number))
    else:
        device = torch.device("cpu")
    print("Device: ", device)
    return device


def makeDir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def delDir(path):
    if os.path.exists(path):
        shutil.rmtree(path)


# def operate_on_dirs_training():
#     makeDir(training_output_path)
#     makeDir(training_models)


def operate_on_dirs_inference():
    makeDir(test_inference_path)
    makeDir(input_path)
    makeDir(output_path)


gpu_number = 0
transform = transforms.Compose([transforms.ToTensor()])
device = get_device(gpu_number)

base_path = os.getcwd()

train_path = os.path.join(base_path, "data", "train")
test_path = os.path.join(base_path, "data", "test")

# training_output_path = os.path.join(base_path, "training_output")
# training_models = os.path.join(base_path, "training_output", "training_models") # for saving plots over training

model_path = os.path.join(base_path, "models")

trained_simple_conv_model = os.path.join(
    base_path, "models", "SimpleConvNet_CrossEntropyLoss_5_epochs.p"
)

test_inference_path = os.path.join(base_path, "data", "inference_on_set_of_images")
input_path = os.path.join(test_inference_path, "input")
output_path = os.path.join(test_inference_path, "output")

# Parameters
ext = ".png"
in_channels = 3
input_size = 28
num_classes = 10
loss_type = "crossentropy"
learning_rate = 0.001
val_pr = 0.1
batch_size = 100
epochs = 5

# for pub sub

key_path = ""
topic_path = ""
subscription_path = ""

# for kafka

topicname = "test"
bootstrapserver = "localhost:9092"
api_name = "kafka"
