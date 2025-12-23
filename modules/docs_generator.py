"""
Module: docs_generator.py
Purpose: Generate documentation from dataset.json
"""

import json
import os

DATASET_PATH = os.path.join(os.path.dirname(__file__), "../dataset/dataset.json")

with open(DATASET_PATH, "r") as file:
    DATASET = json.load(file)


def generate_docs(project_key):
    project = DATASET.get(project_key)
    if project and "docs" in project:
        return project["docs"]
    return f"# No documentation found for '{project_key}'."
