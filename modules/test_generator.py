"""
Module: test_generator.py
Purpose: Generate test cases from dataset.json
"""

import json
import os

DATASET_PATH = os.path.join(os.path.dirname(__file__), "../dataset/dataset.json")

with open(DATASET_PATH, "r") as file:
    DATASET = json.load(file)


def generate_tests(project_key):
    project = DATASET.get(project_key)
    if project and "test" in project:
        return project["test"]
    return f"# No test cases found for '{project_key}'."
