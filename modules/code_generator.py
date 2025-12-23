"""
Module: code_generator.py
Purpose: Generate boilerplate code from dataset.json
"""

import json
import os

DATASET_PATH = os.path.join(os.path.dirname(__file__), "../dataset/dataset.json")

with open(DATASET_PATH, "r") as file:
    DATASET = json.load(file)


def generate_code(project_key):
    project = DATASET.get(project_key)
    if project and "boilerplate" in project:
        return project["boilerplate"]
    return f"# No boilerplate code found for '{project_key}'."
