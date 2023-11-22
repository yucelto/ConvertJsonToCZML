# GeoJSON to CZML Converter

This Python script converts GeoJSON data containing geographic features with optional 3D model information into CZML (Cesium Markup Language) format. CZML is a JSON-based format commonly used for visualizing time-dynamic, geospatial data in the CesiumJS virtual globe.

## Features

- **Dynamic 3D Visualization:** Convert GeoJSON data, including 3D model information, into CZML for dynamic and interactive 3D visualization.

- **Real-World Scaling:** Preserve the real-world dimensions of 3D models, ensuring accurate representation when zooming in or out.

- **Distance-based Visibility:** Control the visibility of models based on viewer distance, optimizing performance and preventing unnecessary rendering at large distances.

## How to Use

1. **Input GeoJSON:** Provide a GeoJSON file with feature geometry and optional properties including unique identifiers, coordinates, and model URLs.

2. **Run the Script:** Execute the Python script, and it will generate a CZML file with the converted data.

3. **Visualize in CesiumJS:** Use the generated CZML file in a CesiumJS application for immersive 3D visualization.

## Dependencies

- Python 3.x

## Notes

- Ensure that the GeoJSON file follows the specified structure with feature properties, including 'Id', 'height', and 'model' (optional).

- Adjust the script parameters for model scaling, minimum pixel size, and distance-based visibility according to your preferences.

## Example Usage

```bash
python geojson_to_czml.py # add input path before run
