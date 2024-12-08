<img  src="https://raw.githubusercontent.com/geoaihub/geoaihub/main/assets/Mersin%20GeoAI%20Hub%202.png"  height=400  width=1000  alt="https://github.com/geoaihub"/>  

<small>Picture Source: <a  href="https://github.com/geoaihub">GeoAI Hub Mersin</a></small>

<br>

This section details the training process undertaken to optimize the performance of YOLO models for detecting collapsed buildings post-earthquake.

<br>

## Overview of YOLO Training

The training involved four YOLO variants: YOLOv7, YOLOv7x, YOLOv8l, and YOLOv8x. Each model was fine-tuned using the curated dataset of annotated VHR satellite images. The key objective was to maximize detection accuracy while maintaining computational efficiency. This comprehensive training approach, paired with robust evaluation metrics, demonstrates the potential of YOLO models in real-world disaster scenarios.

### Training Dataset

Our dataset consists of two of the 41 satellite images from the VHR Maxar Open Data Program, captured on February 11, 2023, at 08:51:47 UTC by the WorldView-2 satellite, covering earthquake-affected areas. These high-resolution images, with a pixel count of 17408x17408 and a pixel resolution of approximately 0.3073 meters, focus on Antakya City, identified by quadkeys 031133023302 and 031133023303. The images are in TIF format and contain WGS 84 / UTM Zone 37N (EPSG 32637) projection information.

From these VHR images, we extracted segments for analysis. A 6400x6400 pixel sub-frame was used for training, and a 3840x3840 pixel sub-frame was employed for validation of YOLO models. These sub-frames were cropped into a grid, resulting in 100 training images and 36 validation images. Each image covers approximately **196.68 meters** in both longitude and latitude, with a total area of **38,681.93 m²**.

The cropped images were centered on reference points to ensure optimal alignment. To further enhance the dataset, we systematically shifted the images by 256 pixels in eight directions from the reference points, generating a total of 1224 images—900 for training and **324 for validation**. After filtering for the most suitable images, we selected 344 training images and **124 validation images**. These images were annotated for collapsed and non-collapsed buildings. The curated dataset was then used for training. The trained model's predictions were applied to the original images, each with a frame size of 17248x17248 pixels, covering the city center of Antakya. This process enabled us to determine the geographic locations of both collapsed and non-collapsed buildings.

- **Number of Images:** 344 training and 124 validation images.
- **Resolution:** 640x640 pixels per image after preprocessing.
- **Annotation Types:** Bounding boxes for collapsed and non-collapsed buildings.

### Training Environment
- **Hardware:** NVIDIA T4 GPU with 16GB memory.
- **Framework:** PyTorch-based implementation using the Ultralytics library.
- **Optimization Algorithm:** Stochastic Gradient Descent (SGD) and AdamW with momentum.

### Hyperparameters
| Parameter          | YOLOv7/YOLOv7x | YOLOv8l/YOLOv8x |
|--------------------|----------------|-----------------|
| Epochs            | 64             | 64              |
| Batch Size        | 8              | 16              |
| Learning Rate     | 0.01           | 0.01            |
| Image Size        | 640x640        | 640x640         |
| Optimizer        | SGD       | AdamW         |

<br>

## Performance Metrics

### Evaluation Metrics
1. **Precision:** Measures the proportion of true positive detections among all positive detections.
2. **Recall:** Measures the proportion of true positive detections among all actual positives.
3. **Mean Average Precision (mAP):**
   - **mAP@.5:** Detection accuracy at a 0.5 IoU threshold.
   - **mAP@.5:.95:** Detection accuracy averaged over IoU thresholds from 0.5 to 0.95.

### YOLOv7 Results
- **mAP@.5:** 0.79
- **Precision:** 0.80
- **Recall:** 0.69
- **F1 Score:** Balanced precision and recall performance.

<img src="https://raw.githubusercontent.com/geoaihub/IGARSS-EQ-Object-Detection-YOLO-Kahramanmaras/refs/heads/main/assets/mAP50_with_zoom_2.png" alt="mAP50 Comparsion Across Models"/>

YOLOv7 achieved the best balance of precision and recall, making it the most effective variant for this application. In comparison, YOLOv8 showed slightly lower precision but demonstrated higher efficiency, particularly in handling larger batch sizes. This tradeoff highlights YOLOv7 as the preferred choice for accuracy, while YOLOv8 may be more suitable for scenarios where processing efficiency is prioritized. For detailed results for all models, please refer to the **[Evaluation.xlsx](https://github.com/geoaihub/IGARSS-EQ-Object-Detection-YOLO-Kahramanmaras/blob/main/1-Training/Evaluation.xlsx)** excel sheet.

<br>

## Challenges and Limitations
- **Misclassifications:**
  - Instances of non-building structures, such as greenhouses, being incorrectly labeled.
- **Dataset Diversity:** Limited variety in building styles and damage types affects generalization.

This comprehensive training approach, paired with robust evaluation metrics, demonstrates the potential of YOLO models in real-world disaster scenarios.
