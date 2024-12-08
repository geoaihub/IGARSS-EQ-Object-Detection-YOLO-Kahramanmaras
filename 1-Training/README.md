<img  src="https://raw.githubusercontent.com/geoaihub/geoaihub/main/assets/Mersin%20GeoAI%20Hub%202.png"  height=400  width=1000  alt="https://github.com/geoaihub"/>  

<small>Picture Source: <a  href="https://github.com/geoaihub">GeoAI Hub Mersin</a></small>

<br>

This section details the training process undertaken to optimize the performance of YOLO models for detecting collapsed buildings post-earthquake.

## Overview of YOLO Training

The training involved four YOLO variants: YOLOv7, YOLOv7x, YOLOv8l, and YOLOv8x. Each model was fine-tuned using the curated dataset of annotated VHR satellite images. The key objective was to maximize detection accuracy while maintaining computational efficiency.

### Training Dataset
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

For detailed results for all models, please refer to the **[Evaluation.xlsx](https://github.com/RSandAI/Comprehensive-YOLO-Airplane-Detection/tree/main/4-Comprehensive%20Inference)** excel sheet.

![mAP50 Graph](mAP50_graph_placeholder.png)

<img src="" alt=""/>

### Training Insights
- **YOLOv7:** Achieved the best balance of precision and recall, making it the most effective variant for this application.
- **YOLOv8:** Showcased slightly lower precision but higher efficiency in handling larger batch sizes.

## Challenges and Limitations
- **Misclassifications:**
  - Instances of non-building structures, such as greenhouses, being incorrectly labeled.
- **Dataset Diversity:** Limited variety in building styles and damage types affects generalization.

This comprehensive training approach, paired with robust evaluation metrics, demonstrates the potential of YOLO models in real-world disaster scenarios.