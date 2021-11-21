__Part 1 :)__
- __original data__ - Contains FashionMNIST folder downloaded as is which has two folders namely "raw" & "processed". The raw folder contains "ubyte" files. 

Note: The following script downloads the data into the mentioned data_path
```
from torchvision import datasets

data = datasets.FashionMNIST(data_path, download=True, train=True)
```
- __`mnist_to_png.py`__ - This python file helps to convert the ubyte data to "png" and generates test & train folders ib the data folder. This enables an easier way to extend this code base to a train and test on larger datasets with images. The test and train folders contain, folders corresponding to each label and their respective images 

- __data__ - Contains image data of FashionMNIST
  - __train__ - folder
    - __0__ - class 0 with and its corresponding images 
    - __1__ - class 1 with and its corresponding images 
    - __2__ - & so on
    - ...
  - __test__ - similar structure to train folder
  - __inference_on_set_of_images__ - helps to run inference on a set of images from a folder
    - __input__ - contains few images to test
    - __output__ - contains the `output.csv` generated from the above input
- __code__ - Contains all the code related to the classification
  - __`config.py`__ - Contains all required paths & parameters
  - __`train.py`__ - This python file helps to train
  - __`inference.py`__ - This python file helps run inference on the test set and also a set of images from a folder. It can print out the confusion matrix and/or the classification report.
  - __utils__ - Contains necessary scripts
    - `dataset.py` - This python file contains a class that loads the data and returns the data loaders
    - `network.py` - Python file that contains the network architectures as classes
    - `trainer.py` - Python file that contains a generic class for training
  -__test_scripts__ - Unit tests for Dataset and Network classes
   - __`test_dataset_class.py`__ - This python file contains a unit test to test `dataset.py` from utils
   - __`test_network_class.py`__ - This python file contains a unit test to test `network.py` from utils

- __models__ - Contains all trained models
  - __`SimpleConvNet_CrossEntropyLoss_20_epochs.p`__ 


### Steps

1. ```virtualenv -p python3 venv```
2. ```source venv/bin/activate```
3. ```cd code```
4. ```pip install -r requirements.txt```
5. ```cd ..```
6.  Download the data into the original_data folder
7. ``` python mnist_to_png.py```
8. Run test scripts if you wanna test but not necessary
9. Make sure you have everything okay in ```config.py```
10. ``` python train.py```
11. ``` python inference.py``` - generates classification report of the test set. Overall accuracy ```~91%``` at this moment.

### Note

1. This code has been completely developed on Ubuntu 18.04 and not been tested on windows. I'm confident that it is written in such a way that it is OS agnostic but just in case if something comes up, feel free to reach out.

2. Replace the data and change your parameters in the config and you should be able to test this library on new datasets. :)

<!---
### Folder Structure

.
├── code
│   ├── config.py
│   ├── inference.py
│   ├── requirements.txt
│   ├── test_dataset_class.py
│   ├── test_network_class.py
│   ├── train.py
│   └── utils
│       ├── dataset.py
│       ├── network.py
│       └── trainer.py
├── data
│   ├── inference_on_set_of_images
│   │   ├── input
│   │   └── output
│   ├── test
│   │   ├── 1
│   │   ├── 2
│   │   └── 3
│   └── train
│       ├── 1
│       ├── 2
│       └── 3
├── mnist_to_png.py
├── models
│   ├── SimpleConvNet_CrossEntropyLoss_20_epochs.p
│   ├── SimpleConvNet_CrossEntropyLoss_3_epochs.p
│   └── SimpleConvNet_CrossEntropyLoss_5_epochs.p
├── original_data
│   └── FashionMNIST
│       ├── processed
│       └── raw
└── README.md
-->


