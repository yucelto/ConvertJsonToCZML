import json
import os

def geojson_to_czml(input_geojson_path):
    with open(input_geojson_path, 'r') as geojson_file:
        geojson_data = json.load(geojson_file)

    czml_output = [
        {
            'id': 'document',
            'name': 'CZML Model',
            'version': '1.0',
        }
    ]

    for feature in geojson_data['features']:
        czml_feature = {
            'id': str(feature['properties']['Id']),
            'name': str(feature['properties']['Id']),
            'position': {
                'cartographicDegrees': [
                    feature['geometry']['coordinates'][0],
                    feature['geometry']['coordinates'][1],
                    feature['properties']['height'] if 'height' in feature['properties'] else 0
                ]
            },
        }

        if 'model' in feature['properties']:
            czml_feature['model'] = {
                'gltf': feature['properties']['model'],
                'scale': 1.0,
                'disableDepthTestDistance': "NaN",
                'distanceDisplayCondition': {
                'distanceDisplayCondition': [
                    0,
                    1800
                 ]
                },
            }

        czml_output.append(czml_feature)

    output_czml_path = os.path.splitext(input_geojson_path)[0] + '_output.czml'

    with open(output_czml_path, 'w') as czml_file:
        json.dump(czml_output, czml_file, indent=2)

if __name__ == "__main__":
    input_geojson_path = 'your-file-path/test-file.json'
    geojson_to_czml(input_geojson_path)
