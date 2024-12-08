
# A Geospatial Dataframe Of Collapsed Buildings in Antakya City After The 2023 Kahramanmaraş Earthquakes Using Object Detection Based on YOLO and VHR Satellite Images

<img  src="https://raw.githubusercontent.com/geoaihub/geoaihub/main/assets/Mersin%20GeoAI%20Hub%202.png"  height=400  width=1000  alt="https://github.com/geoaihub"/>  

<small>Picture Source: <a  href="https://github.com/geoaihub">GeoAI Hub Mersin</a></small>

<br>


This repository contains weights, evaluation metrics, and detailed training information for various YOLO architectures trained on high-resolution satellite imagery for detecting collapsed buildings, leveraging data sourced from Maxar Technologies' Very High-Resolution (VHR) satellite imagery. The dataset includes images of Antakya City, impacted by the 2023 Kahramanmaraş earthquake, captured by the WorldView-2 satellite. This study employs YOLOv7, YOLOv7x, YOLOv8l, and YOLOv8x models, each trained using different hyperparameters and data augmentation techniques. The models were evaluated on a curated dataset, which includes manually annotated collapsed and non-collapsed buildings.

Key highlights of the analysis include:

-   Training on images segmented from the original high-resolution satellite data, with preprocessing steps such as cropping and augmentation to create a robust training and validation set.
-   Performance metrics such as Precision, Recall, and Mean Average Precision (mAP) were evaluated at IoU thresholds of 0.5 and 0.5:0.95. YOLOv7 demonstrated a mAP@.5 of 0.79.
-   Integration with Geographic Information Systems (GIS) for precise coordinate localization, providing geospatial data for disaster response efforts.

This work combines real-time object detection with GIS-based analysis to generate actionable insights for post-disaster damage assessment. Below are the detailed metrics, model weights, and download links for each trained YOLO architecture.

## Updates

**A Geospatial Dataframe Of Collapsed Buildings in Antakya City After The 2023 Kahramanmaraş Earthquakes Using Object Detection Based on YOLO and VHR Satellite Images paper is now available!**

<details>
<summary>Latest updates...</summary>

<br>

**July 2024** 
- Project successfully presenten on Athens/Greece on IEEE IGARSS 2024!

**March 2024**  
- Paper accepted to make an oral presentation on Athens/Greece on IEEE IGARSS 2024!

**September 2023**  
- Models evaluated and made predictions on Antakya City Center.
  
**August 2023**  
- Build dataset to train and validate YOLO models. Utilized Maxar Open Data Program to get VHR images.
- Experiments completed! YOLOv7 and YOLOv8 models were trained.

</details>

<br>

## Dataset

The dataset used in this study was sourced from Maxar Technologies' Very High-Resolution (VHR) satellite imagery, made accessible through the Maxar Open Data Program. Two high-resolution images, captured on February 11, 2023, at 08:51:47 UTC by the WorldView-2 satellite, form the backbone of the dataset. These images:

- Covered Antakya City, heavily affected by the 2023 Kahramanmaraş earthquake.
- Had a resolution of 17408x17408 pixels and approximately 0.3073 meters per pixel.
- Incorporated WGS 84 / UTM Zone 37N (EPSG 32637) projection data.

To ensure robust training and validation:

1. **Cropping and Preprocessing:** The original images were segmented into smaller sub-frames:
   - **Training sub-frame:** 6400x6400 pixels.
   - **Validation sub-frame:** 3840x3840 pixels.
   - Each segment covered approximately 38681.93 m².

2. **Grid Division:** Cropping generated 100 training and 36 validation images, each centered at reference points for alignment.

3. **Augmentation:** Images were systematically shifted by 256 pixels in eight directions, resulting in 1224 augmented images. Following quality filtering, the dataset comprised:
   - **Training Images:** 344.
   - **Validation Images:** 124.

4. **Annotation:** Collapsed and non-collapsed buildings were manually annotated. These annotations formed the basis for model training and evaluation.

This curated dataset was pivotal in detecting collapsed structures and accurately mapping their geolocations.

## Training

The YOLO framework, known for its real-time object detection capabilities, was utilized. Four YOLO variants—YOLOv7, YOLOv7x, YOLOv8l, and YOLOv8x—were trained on the dataset. Key highlights include:

1. **Model Selection:**
   - **YOLOv7** outperformed others in balancing speed and accuracy.
   - Features such as E-ELAN enhanced learning by diversifying feature extraction.

2. **Hyperparameters:**
   - **Epochs:** 64.
   - **Batch Size:** 8 for YOLOv7 and YOLOv7x; 16 for YOLOv8l and YOLOv8x.
   - **Learning Rate:** 0.01.
   - **Image Size:** 640x640 pixels.

3. **Performance Metrics:**
   - Precision, Recall, and Mean Average Precision (mAP) at IoU thresholds of 0.5 and 0.5:0.95.
   - YOLOv7 achieved a mAP@.5 of 0.79, showcasing its robustness in detecting collapsed buildings.

4. **Evaluation:**
   - Predictions were visualized as Geo-DataFrames, integrating bounding box details, object types, probabilities, and geographic coordinates.
   - Heatmaps and clustering visualizations provided insights into the spatial distribution of collapsed structures.

### Access to the Details

For those interested in a deeper analysis, all experimental configurations, results, and detailed performance metrics have been documented and made available through a comprehensive **[spreadsheet of experiment results]()**. This document contains all the specifics of the experiments conducted, including model hyperparameters, optimizer settings, and corresponding performance metrics, offering full transparency into the experimental process. Here you can find all the details about the training process: **[1-Training]().**

<br>

## Coordinate Localization


A distinguishing feature of this study was the integration of object detection results into a Geographic Information System (GIS). To enhance the precision and automation of geographic coordinate calculations, we developed the **InferenceVision** library. This tool calculates the geographic coordinates of detected objects from bounding boxes and other metadata. Key steps include:

1. **Geospatial Data Generation:**
   - Bounding boxes from detected collapsed buildings were used as inputs for **InferenceVision** to derive geographic coordinates.
   - Each detection included metadata such as object type, confidence scores, and bounding box dimensions, which were processed to calculate geographic coordinates.
   
2. **Spatial Visualization:**
   - Visual tools like **Folium** were employed to:
     - Create heatmaps indicating collapsed building density.
     - Add markers and popups with precise geolocations and address information.
   
3. **Application:**
   - The geospatial data generated with **InferenceVision** provided actionable insights for disaster response and recovery efforts.
   - Collapsed buildings in Antakya City were distributed across 28.20 km², with detailed mapping aiding efficient resource allocation.
   
4. **Challenges:**
   - Misclassification of non-building structures (e.g., greenhouses).
   - Context-specific limitations requiring diverse datasets for improved generalizability.

By leveraging **InferenceVision**, the process of transforming bounding box detections into actionable geospatial data was streamlined, improving the overall accuracy of disaster damage mapping and response efforts. 

For more information on the **InferenceVision** library, please visit our [website](https://doguilmak.github.io/InferenceVision/), where you'll find detailed documentation and resources.


### Access to the Details

For a more detailed look at the results, please refer to the full documentation available in the **[2-Coordinate Localization]()**.

<br>

By combining YOLO’s object detection prowess with GIS-based geospatial analysis, this study demonstrates a comprehensive framework for post-earthquake damage assessment.

## Citation

If this dataset or model weights benefit your research, please cite our [paper]().

<br>