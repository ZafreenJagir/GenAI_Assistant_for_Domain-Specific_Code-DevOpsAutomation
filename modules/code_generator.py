"""
Module: code_generator.py
Purpose: Generate boilerplate code from dataset.json
"""

import json
import os

DATASET_PATH = os.path.join(os.path.dirname(__file__), "../dataset/dataset.json")

with open(DATASET_PATH, "r") as file:
    DATASET = json.load(file)


def generate_code(project_key, language="python"):
    project = DATASET.get(project_key)

    if project:
        # language-specific boilerplate
        if "boilerplate" in project:
            if isinstance(project["boilerplate"], dict):
                return project["boilerplate"].get(
                    language,
                    f"# Boilerplate not available for {language}"
                )
            return project["boilerplate"]

    return f"# No boilerplate code found for '{project_key}'."
