# Food_Vision_mini


## 💭 What this project does

I wanted to have a more hands-on experience in machine learning, so I decided to make a food image classification program. My program can take an image of either a "sushi", "pizza" or a "steak" and would be able to return a conclusion on what that image actually is

## 💡 What I implemented

In this program I implemented multiple different models to test which model has the highest accuracy in classifying if an image contains either a sushi, pizza or steak.

My test results are shown on <a href="https://github.com/Moonshallow5/Food_Vision_mini/blob/main/results.txt"> results.txt</a>, where I used pre-trained pytorch models of efficinentnetb2 and resnet50, as well as my own model which has a much lower accuracy.

Furthermore, I also implemented my own custom implementation in <a href="https://github.com/Moonshallow5/Food_Vision_mini/blob/main/model_architecture.py">model_architecture.py</a>, where a TinyVGG and VGG16 is implemented, which has much lower test accuracy as it isn't a pre-trained model and i have a small selection of datasets

Here are <a href="https://github.com/Moonshallow5/Food_Vision_mini/blob/main/effnet_b2_7_epochs_without_aug.png">Effnet_b2</a> and <a href="https://github.com/Moonshallow5/Food_Vision_mini/blob/main/resnet50_7_epochs_without_aug.png">resnet50</a> test results on 7 epochs without any data augmentation 


Learn about MLflow as well as Nsight systems to optimize my program and see for any potential bottlenecks as well

## 👀Live preview

I wanted to show my project in live-action so I made a link to my <a href="https://huggingface.co/spaces/Moonshallow5/FoodVision_mini?logs=container">HuggingFace</a> account where there is already an app running on gradio for anyone to use. The model used in HuggingFace and in my <a href="https://github.com/Moonshallow5/Food_Vision_Flutter">Flutter project</a>  are models which were trained in this repo.

## 🔧Further implementations 

- [x] I want to turn this program into a Flutter API for anyone to use it on their mobile phones, but this would take me some time to lern Dart documentations



