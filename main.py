from torch import nn
import torch
from torchvision import transforms
import torchvision
import os
from pathlib import Path
import requests
import data_setup
import engine


from torchmetrics import Accuracy
from model_architecture import *


from tqdm.auto import tqdm


device='cpu'






data_20_percent_path = "data\pizza_steak_sushi_20_percent"
train_dir_20_percent = data_20_percent_path+"\\train"
test_dir = data_20_percent_path+"\\test"


# Create a transform to normalize data distribution to be inline with ImageNet
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], # values per colour channel [red, green, blue]
                                 std=[0.229, 0.224, 0.225])

# Create a transform pipeline
simple_transform = transforms.Compose([
                                       transforms.RandomResizedCrop(260),        # Randomly crop the image and resize to 260x260
                                        transforms.RandomHorizontalFlip(),
                                       transforms.ToTensor(), # get image values between 0 & 1
                                       normalize
])

BATCH_SIZE=32





def set_seeds(seed=42):
    torch.manual_seed(42)
    torch.cuda.manual_seed(42)


def create_effnetb2(out_features=3):
    
    weights = torchvision.models.EfficientNet_B2_Weights.DEFAULT
    transforms=weights.transforms()
    model = torchvision.models.efficientnet_b2(weights=weights).to('cpu')
    dropout=0.3
    in_features=1408
    #for param in model.features.parameters():
     # param.requires_grad=False
    torch.manual_seed(seed=42)
    
    

    # Update the classifier head
    model.classifier = nn.Sequential(
        nn.Dropout(p=dropout, inplace=True),
        nn.Linear(in_features=in_features, 
                  out_features=out_features)
    ).to('cpu') 

    # Set the model name
    model.name = "effnetb2"
    return model,transforms

model_1,effnetb2_transforms=create_effnetb2(out_features=3)

train_dataloader_20_percent, test_dataloader, class_names = data_setup.create_dataloaders(train_dir=train_dir_20_percent,
                                                                                          test_dir=test_dir,
                                                                                          transform=effnetb2_transforms,
                                                                                          batch_size=BATCH_SIZE)

def create_resNet50(out_features=3):
    weights = torchvision.models.ResNet50_Weights.DEFAULT
    model = torchvision.models.resnet50(weights=weights).to(device)
    
    dropout=0.3
    in_features=model.fc.in_features
    for param in model.parameters():
        param.requires_grad = False
    
    # Set the seeds
    # Update the classifier head
    model.fc = nn.Sequential(
        nn.Dropout(p=dropout, inplace=True),
        nn.Linear(in_features=in_features, 
                  out_features=out_features)
    ).to(device) 

    # Set the model name
    model.name = "resnet50"
    return model


model_2=create_resNet50(3)

model_3=VGG16(3)

model_4=TinyVGG(3)
model_4.name="tinyvgg"
model_3.name="vgg16"
model_6=Model2BestOnPaper2((3,260,260),3)
model_6.name="model2Best"




loss_fn = nn.CrossEntropyLoss()
optimizer =torch.optim.Adam(model_1.parameters(), lr=0.001)

from helper_functions import *

from utils import *


if __name__ == "__main__":
    from torch.utils.mobile_optimizer import optimize_for_mobile
    set_seeds()

    device='cpu'
   
    '''Code below trains the efficientnet_b2 model with training data'''
    engine.train(model=model_1,train_dataloader=train_dataloader_20_percent,test_dataloader=test_dataloader,optimizer=optimizer,loss_fn=loss_fn,epochs=7,device='cpu')
    
    
    '''
    My code below produces a Torchscript model of my best performing PyTorch model, to run on Flutter
    '''

    '''
    model_1.eval()
    
    traced_model = torch.jit.script(model_1)
    optimized_traced_model = optimize_for_mobile(traced_model)
    optimized_traced_model._save_for_lite_interpreter("pre_model_10_script_cpu_transforms_unfreeze.pt")
    
    '''
    
    
    



    
   