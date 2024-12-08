<img  src="https://raw.githubusercontent.com/geoaihub/geoaihub/main/assets/Mersin%20GeoAI%20Hub%202.png"  height=400  width=1000  alt="https://github.com/geoaihub"/>  

<small>Picture Source: <a  href="https://github.com/geoaihub">GeoAI Hub Mersin</a></small>

<br>

This section highlights the Coordinate Localization process used to generate precise geographic insights post-inference. Prediction results covered approximately **28 km²** in the Antakya City Center.

## Overview

Coordinate localization involved:
- Mapping the predicted bounding boxes to geographic coordinates.
- Visualizing prediction results using heatmaps and marker maps for clarity.

### Prediction Inference

Prediction inference map illustrates the YOLOv7 predictions, displaying a map that highlights both collapsed and non-collapsed buildings in the disaster-stricken area. The analysis covers an area of approximately 28.20 km² in the city center of Antakya, with predictions made on 729 high-resolution image frames. The object detection process demonstrated high efficiency, successfully identifying 7,037 buildings in just 47.241 seconds.

<img src="" alt=""/>

### Heatmap

The heatmap illustrates the spatial density of collapsed buildings across the region. High-density areas are represented with warmer colors (e.g., red).

![Heatmap](heatmap_marker.png)

<img src="" alt=""/>

### Marker Map

The marker map displays individual collapsed building predictions. Each marker provides detailed metadata:
- **Latitude and Longitude** of the prediction.
- Associated **image** filename.
- Building **ID** and predicted **class** (e.g., "collapsed").
- **Probability** score indicating prediction confidence.

### Example Marker Metadata
```plaintext
Latitude: 36.208237417
Longitude: 36.158416564
Image: /content/images/image_677.tif
Building ID: 5
Class: collapsed
Probability: 0.78173601789622
```

## Key Insights

1. **Density Analysis:**
   - The heatmap highlights clusters of damage, aiding prioritization for on-ground response efforts.

2. **Granular Predictions:**
   - The marker map offers precise, building-level predictions for further verification and analysis.

This dual visualization approach ensures comprehensive situational awareness, combining high-level trends with detailed observations.

