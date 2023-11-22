import os
import json


def generate_sample_data():
    file_path = os.path.join(os.path.dirname(__file__), '../data/data.json')
    with open(file_path) as f:
        return json.load(f)


def generate_expected_data():
    data = generate_sample_data()
    for product in data["products"]:
        yield product
