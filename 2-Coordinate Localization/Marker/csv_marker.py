# -*- coding: utf-8 -*-
"""csv_marker.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hBNuG6Da_LV5myi78QCloVXC8-Qxa3Up

<h1 align=center><b>Collapsed Building Interactive Maps with Markers and Popups Using Folium</b></font></h1>

<br>

<p align="center">
    <img src="https://drive.google.com/uc?id=1dx98iliCTjuonFHX_orRz20O8S7CeTnW" height=300 width=2000 alt="GitHub">
</p>

<small>Picture Source: <a href="https://github.com/doguilmak">Doğu İlmak</a></small>

<br>

**Folium for Interactive Maps with Markers and Popups:**

Folium is a Python library that facilitates the creation of interactive maps and visualizations on web browsers. It's built on the Leaflet JavaScript library, known for its interactive mapping capabilities. Folium allows you to craft maps with diverse features such as markers, popups, choropleths, and heatmaps, all of which can be displayed interactively using HTML.

<br>

**Key Features and Concepts:**

1.  **Map Creation:** Generate maps effortlessly by specifying the center's latitude, longitude, and initial zoom level. A basic map can be produced with a single line of code.
    
2.  **Markers and Popups:** Integrate markers onto the map to pinpoint specific points of interest. Each marker can be accompanied by a popup, revealing additional information when interacted with.
    
3.  **Choropleths:** Enable choropleth maps to color areas (like countries or regions) based on numeric values. This is valuable for depicting geographical variations in data.
    
4.  **Heatmaps:** Utilize heatmaps to visualize the density or intensity of data points across the map. Folium's HeatMap plugin simplifies the creation of heatmaps from a list of coordinates.
    
5.  **Layer Control:** Incorporate multiple layers into a map and offer users the ability to toggle between them. This feature is particularly handy for displaying diverse datasets or overlays within a single map.
    
6.  **Plugins and Extensions:** Extend Folium's capabilities with plugins and extensions. These include tools for clustering markers, drawing shapes, and more.
    
7.  **Export to HTML:** After crafting a map using Folium, save it as an interactive HTML file. This HTML file can be opened in web browsers to engage with the map interactively.
    
8.  **Integration with Pandas:** Seamlessly blend Folium with Pandas DataFrames, simplifying the visualization of data directly from your data structures.
    
<br>

**Benefits:**

Folium is an excellent tool for sharing interactive maps with others without necessitating specialized software installation. It's widely employed for visualizing geospatial data, generating interactive dashboards, and presenting insights visually.

While Folium is a powerful choice, remember that there are other geospatial visualization libraries available in Python. Depending on your specific requirements and the complexity of your analysis, exploring options like Geopandas can offer even more advanced geospatial capabilities.
"""

import folium
import pandas as pd

data = pd.read_csv('/content/collapsed_data.csv')

data.head()

center_lat = data['Latitude'].mean()
center_lon = data['Longitude'].mean()

m = folium.Map(location=[center_lat, center_lon], zoom_start=10)

for index, row in data.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']],
                  popup=f"<b>Latitude:</b> {row['Latitude']}<br><b>Longitude:</b> {row['Longitude']}<br><b>Image:</b> {row['Image']}<br><b>Building ID:</b> {row['Point']}<br><b>Class:</b> {row['Object Type']}<br><b>Probability:</b> {row['Probability']}").add_to(m)

m.save('map_with_markers.html')

from google.colab import files
files.download('/content/map_with_markers.html')

"""# Contact Me
<p>If you have something to say to me please contact me:</p>

<ul>
  <li>Twitter: <a href="https://twitter.com/Doguilmak">Doguilmak</a></li>
  <li>Mail address: doguilmak@gmail.com</li>
</ul>
"""

from datetime import datetime
print(f"Changes have been made to the project on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")