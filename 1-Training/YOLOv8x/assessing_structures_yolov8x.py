# -*- coding: utf-8 -*-
"""assessing_structures_YOLOv8x.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yFgfv7lClHwxcZ4BzLi_UmDhoTZyX7yC

# Building Detection from High-Resolution Satellite Images Using YOLOv8x: Assessing Collapsed and Non-Collapsed Structures

<br>

<img  src="https://raw.githubusercontent.com/geoaihub/geoaihub/main/assets/Mersin%20GeoAI%20Hub%202.png"  height=400  width=1000  alt="https://github.com/geoaihub"/>  

<small>Picture Source: <a  href="https://github.com/geoaihub">GeoAI Hub Mersin</a></small>

<br>

## Introduction
In recent years, the field of computer vision has witnessed remarkable advancements, empowering various applications ranging from autonomous driving to surveillance systems. One critical task within computer vision is the detection and localization of objects within images. This capability finds particular relevance in disaster management, urban planning, and infrastructure assessment, where the accurate identification of buildings from satellite imagery plays a crucial role. In this scientific project, we present an approach for collapsed and non-collapsed building detection using YOLOv8x, a state-of-the-art object detection algorithm, applied to high-resolution satellite images obtained from Maxar. By harnessing the power of deep learning and leveraging the spatial details captured by these satellite images, we aim to contribute to the field of disaster response and urban infrastructure analysis.

<br>

The dataset utilized in this project consists of 900 high-resolution satellite images, which were carefully selected to represent diverse urban environments. Out of these, 334 distinct images were used for training the YOLOv8 model, while 124 images were reserved for validation purposes. The training images were specifically chosen to encompass a wide range of building sizes, orientations, and structural complexities, ensuring the robustness and generalization of the model.

<br>

The YOLOv8 algorithm, short for "You Only Look Once version 7," is renowned for its real-time object detection capabilities and high accuracy. It utilizes a deep neural network architecture to simultaneously predict bounding boxes and class probabilities for multiple objects within an image. This holistic approach not only ensures rapid inference times but also provides a comprehensive understanding of the spatial distribution of buildings in the satellite images. To facilitate training and evaluation, all images were resized to a resolution of 640x640 pixels. The YOLOv8 model was then trained using a combination of advanced optimization techniques, including stochastic gradient descent and backpropagation, to iteratively improve its ability to detect collapsed and non-collapsed buildings accurately. Throughout the training process, the model learns to recognize distinctive features and patterns associated with buildings, enabling it to make accurate predictions on unseen data.

<br>

The validation dataset consisting of 124 images served as a benchmark for evaluating the performance of our trained model. By comparing the predicted bounding boxes with ground truth annotations, we measured metrics such as precision, recall, and F1 score, quantifying the model's ability to correctly detect buildings and distinguish between collapsed and non-collapsed structures. Through this scientific project, we aim to contribute to the ongoing efforts in disaster management and urban planning by providing a robust and efficient method for building detection from high-resolution satellite images. The accurate identification of collapsed structures can significantly aid search and rescue operations in disaster-stricken areas, while the detection of intact buildings can assist in assessing urban development and infrastructure planning.

<br>

In the subsequent sections, we will delve into the methodology employed, discuss the experimental setup, present the results obtained, and analyze the performance of the YOLOv8x model in detecting collapsed and non-collapsed buildings. This research represents a stepping stone towards the development of automated systems for rapid assessment and response during critical situations, ultimately contributing to the resilience and safety of our cities and communities.

<br>

Since its introduction, YOLO has undergone several improvements and variations. Different versions such as YOLOv2, YOLOv3, and YOLOv4 have been developed, each introducing enhancements in terms of accuracy, speed, and additional features.

It's important to note that this is a high-level overview of YOLO, and the algorithm has many technical details and variations. For a more in-depth understanding, it's recommended to refer to the original YOLO papers and related resources.

<br>

## Keywords

*   Building detection
*   YOLOv8
*   Object detection
*   High-resolution satellite images
*   Disaster management
*   Urban planning
*   Deep learning
*   Object detection
*   Collapsed structures

<br>

Make sure your runtime is **GPU** (_not_ CPU or TPU). And if it is an option, make sure you are using _Python 3_. You can select these settings by going to `Runtime -> Change runtime type -> Select the above mentioned settings and then press SAVE`.
"""

import os

import pandas as pd

from IPython.display import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
from PIL import Image

from google.colab import files
from google.colab import drive

import warnings
warnings.filterwarnings("ignore")

"""## Data Pre-processing"""

!pip install ultralytics -q

!unzip -q /content/data.zip

# !rm -rf /content/data.zip

#@markdown ---
#@markdown ### Enter image paths:
train_images_dir = "/content/train/images" #@param {type:"string"}
val_images_dir = "/content/val/images" #@param {type:"string"}

train_image_count = len([f for f in os.listdir(train_images_dir) if f.endswith(".png")])
val_image_count = len([f for f in os.listdir(val_images_dir) if f.endswith(".png")])

print(f"Number of images in train folder: {train_image_count}")
print(f"Number of images in val folder: {val_image_count}")

#@markdown ---
#@markdown ### Enter label paths:
train_labels_dir = "/content/train/labels" #@param {type:"string"}
val_labels_dir = "/content/val/labels" #@param {type:"string"}

train_txt_count = len([f for f in os.listdir(train_labels_dir) if f.endswith(".txt")])
val_txt_count = len([f for f in os.listdir(val_labels_dir) if f.endswith(".txt")])

print(f"Number of TXT files in train labels folder: {train_txt_count}")
print(f"Number of TXT files in val labels folder: {val_txt_count}")

#@markdown You can plot any image and labels you want.

#@markdown `classes = {0: collapsed, 1: non_collapsed}`

image_path = 'train/images/image_17.png' #@param {type:"string"}
label_path = 'train/labels/image_17.txt' #@param {type:"string"}

image = Image.open(image_path)
image_width, image_height = image.size
fig, ax = plt.subplots(1)
ax.imshow(image)

unique_classes = {}

with open(label_path, 'r') as file:
    for line in file:

        class_label, x, y, width, height = line.split()

        x = float(x) * image_width
        y = float(y) * image_height
        width = float(width) * image_width
        height = float(height) * image_height

        x_min = x - width / 2
        y_min = y - height / 2

        if class_label not in unique_classes:
            unique_classes[class_label] = f"C{len(unique_classes) + 1}"

        box_color = unique_classes[class_label]

        rect = patches.Rectangle((x_min, y_min), width, height, linewidth=1, edgecolor=box_color, facecolor='none')
        ax.add_patch(rect)


ax.set_aspect('equal')
legend_handles = [patches.Patch(color=color, label=f"Class {label}") for label, color in unique_classes.items()]
ax.legend(handles=legend_handles)
plt.show()

"""## Training

Model link: [ultralytics GitHub](https://github.com/ultralytics/ultralytics)
"""

from ultralytics import YOLO, checks
import torch
checks()

torch.__version__

!wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8x.pt

model = YOLO("/content/yolov8x.pt")

model

coco_yaml_path = '/content/coco.yaml'

# !yolo train model=/content/yolov8x.pt data=coco.yaml epochs=64 imgsz=640

model.train(data=coco_yaml_path,
            epochs=64,
            imgsz=640)

"""## Model Details and Outputs"""

df = pd.read_csv('/content/runs/detect/train/results.csv')
df

image1 = mpimg.imread('/content/runs/detect/train/labels_correlogram.jpg')
image2 = mpimg.imread('/content/runs/detect/train/labels.jpg')

fig, axes = plt.subplots(1, 2, figsize=(16, 9), dpi=300)
axes[0].imshow(image1)
axes[0].set_title('Correlogram')
axes[0].axis('off')
axes[1].imshow(image2)
axes[1].set_title('Label Distribution')
axes[1].axis('off')
plt.show()

image1 = mpimg.imread('/content/runs/detect/train/confusion_matrix.png')
image2 = mpimg.imread('/content/runs/detect/train/confusion_matrix_normalized.png')

fig, axes = plt.subplots(1, 2, figsize=(16, 9), dpi=300)
axes[0].imshow(image1)
axes[0].set_title('Confusion Matrix')
axes[0].axis('off')
axes[1].imshow(image2)
axes[1].set_title('Confusion Matrix Normalized')
axes[1].axis('off')
plt.show()

image = mpimg.imread('/content/runs/detect/train/results.png')
plt.figure(figsize=(16, 9), dpi=300)
plt.title('Results')
plt.imshow(image)
plt.axis('off')
plt.show()

image1 = mpimg.imread('/content/runs/detect/train/val_batch0_labels.jpg')
image2 = mpimg.imread('/content/runs/detect/train/val_batch0_pred.jpg')

fig, axes = plt.subplots(1, 2, figsize=(16, 9), dpi=300)
axes[0].imshow(image1)
axes[0].set_title('Labels')
axes[0].axis('off')
axes[1].imshow(image2)
axes[1].set_title('Predictions')
axes[1].axis('off')
plt.show()

image1 = mpimg.imread('/content/runs/detect/train/F1_curve.png')
image2 = mpimg.imread('/content/runs/detect/train/PR_curve.png')
image3 = mpimg.imread('/content/runs/detect/train/P_curve.png')
image4 = mpimg.imread('/content/runs/detect/train/R_curve.png')

fig, axes = plt.subplots(2, 2, figsize=(16, 9), dpi=300)
axes[0][0].imshow(image1)
axes[0][0].axis('off')
axes[0][1].imshow(image2)
axes[0][1].axis('off')
axes[1][0].imshow(image3)
axes[1][0].axis('off')
axes[1][1].imshow(image4)
axes[1][1].axis('off')

plt.show()

metrics = model.val()  # no arguments needed, dataset and settings remembered

metrics.box.map    # map50-95

metrics.box.map50  # map50

metrics.box.map75  # map75

metrics.box.maps   # a list contains map50-95 of each category

# results = model('https://ultralytics.com/images/bus.jpg')

# model.export(format='')

"""## Uplad Test Image and Video to Make Prediction

Video Testing:

*   Select a video file that contains satellite image footage.
*   Load the pre-trained YOLOv8 model and its corresponding weights.
*   Utilize the OpenCV library to read and process each frame of the video.
*   Pass each frame through the drone detection model for real-time inference.
*   Draw bounding boxes around detected buildings and display the annotated video output.


Image Testing:

*   Choose an image that includes a building satellite image.
*   Load the pre-trained YOLOv8 model and its weights.
*   Read and process the image.
*   Apply the trained model to the image and identify the presence of a buildings.
*   Visualize the image with a bounding box around the detected buildings, if present.
*   Analyze the model's performance by assessing the correct identification of the buildings.
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/
!mkdir test
# %cd /content/test

uploaded = files.upload()

!yolo predict model=yolov8n.pt source='/content/test/'

"""## Save the Results"""

files.download('/content/runs/detect/train/train_batch0.jpg')
files.download('/content/runs/detect/train/train_batch1.jpg')
files.download('/content/runs/detect/train/train_batch1188.jpg')
files.download('/content/runs/detect/train/train_batch1189.jpg')
files.download('/content/runs/detect/train/train_batch1190.jpg')
files.download('/content/runs/detect/train/train_batch2.jpg')

files.download('/content/runs/detect/train/val_batch0_labels.jpg')
files.download('/content/runs/detect/train/val_batch0_pred.jpg')
files.download('/content/runs/detect/train/val_batch1_labels.jpg')
files.download('/content/runs/detect/train/val_batch1_pred.jpg')
files.download('/content/runs/detect/train/val_batch2_labels.jpg')
files.download('/content/runs/detect/train/val_batch2_pred.jpg')

files.download('/content/runs/detect/train/F1_curve.png')
files.download('/content/runs/detect/train/PR_curve.png')
files.download('/content/runs/detect/train/P_curve.png')
files.download('/content/runs/detect/train/R_curve.png')
files.download('/content/runs/detect/train/confusion_matrix.png')
files.download('/content/runs/detect/train/confusion_matrix_normalized.png')
files.download('/content/runs/detect/train/results.csv')
files.download('/content/runs/detect/train/results.png')
files.download('/content/runs/detect/train/labels.jpg')
files.download('/content/runs/detect/train/labels_correlogram.jpg')
files.download('/content/runs/detect/train/args.yaml')

# files.download('runs/detect/exp/')
files.download('/content/coco.yaml')
files.download('/content/runs/detect/train/weights/best.pt')

"""## Conclusion
In this scientific project, we presented an approach for detecting collapsed and non-collapsed buildings from high-resolution satellite images using the *YOLOv8* object detection algorithm. By leveraging the power of deep learning and utilizing Maxar's high-resolution satellite imagery, we aimed to contribute to disaster response and urban infrastructure analysis. Through careful selection and preprocessing of a dataset comprising 900 satellite images, we trained the *YOLOv8* model using 334 images while reserving 124 images for validation. The model was trained to recognize distinctive features and patterns associated with buildings, enabling it to accurately predict bounding boxes and class probabilities.

<br>

The evaluation of our trained model on the validation dataset revealed promising results. By comparing predicted bounding boxes with ground truth annotations, we measured metrics such as *precision*, *recall*, and *F1 score*, demonstrating the model's ability to detect buildings and differentiate between **collapsed and non-collapsed structures**. Our research represents a significant step towards automated systems for rapid assessment and response during critical situations. The accurate identification of collapsed structures can greatly aid search and rescue operations, while the detection of intact buildings can assist in urban development and infrastructure planning.

<br>

However, there are still areas for improvement and further exploration. The model's performance can be enhanced by incorporating more diverse and extensive datasets, including satellite images from various geographical locations and different disaster scenarios. Additionally, *fine-tuning* the model with additional training iterations and exploring advanced optimization techniques could potentially yield even better results. The application of *deep learning* algorithms for building detection from satellite imagery has enormous potential in various fields, including *disaster management*, *urban planning*, and *infrastructure assessment*. As technology continues to advance, we anticipate further improvements in accuracy, speed, and scalability, making these automated systems invaluable in supporting decision-making processes and enhancing overall safety and resilience.

<br>

In conclusion, our scientific project demonstrates the effectiveness of YOLOv8 in detecting collapsed and non-collapsed buildings from high-resolution satellite images. By bridging the gap between computer vision and remote sensing, we have made significant strides towards leveraging artificial intelligence to enhance disaster response and urban planning, ultimately contributing to the well-being of communities worldwide..

## Contact Me
<p>If you have something to say to me please contact me:</p>

<ul>
  <li>Twitter: <a href="https://twitter.com/Doguilmak">Doguilmak</a></li>
  <li>Mail address: doguilmak@gmail.com</li>
</ul>
"""

from datetime import datetime
print(f"Changes have been made to the project on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")