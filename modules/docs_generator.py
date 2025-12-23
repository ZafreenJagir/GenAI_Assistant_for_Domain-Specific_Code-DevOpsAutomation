"""
Module: docs_generator.py
Purpose: Generate documentation from dataset.json
"""

import json
import os


def generate_docs(project_key, language="python"):
    project = DATASET.get(project_key)

    if project:
        if "docs" in project:
            if isinstance(project["docs"], dict):
                return project["docs"].get(
                    language,
                    f"# No documentation available for {language}"
                )
            return project["docs"]

    return f"# No documentation found for '{project_key}'."
