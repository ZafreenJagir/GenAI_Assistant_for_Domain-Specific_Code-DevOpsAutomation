"""
Module: test_generator.py
Purpose: Generate test cases from dataset.json
"""
import json
import os


def generate_tests(project_key, language="python"):
    project = DATASET.get(project_key)

    if project:
        if "test" in project:
            if isinstance(project["test"], dict):
                return project["test"].get(
                    language,
                    f"# No tests available for {language}"
                )
            return project["test"]

    return f"# No test cases found for '{project_key}'."
