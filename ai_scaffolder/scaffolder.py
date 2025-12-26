import json
import os


def generate_project(template_path: str):
    if not os.path.exists(template_path):
        raise FileNotFoundError("Template file not found.")

    with open(template_path, "r", encoding="utf-8") as f:
        template = json.load(f)

    project_name = template.get("project_name")
    structure = template.get("structure")

    if not project_name or not structure:
        raise ValueError("Invalid template format.")

    os.makedirs(project_name, exist_ok=True)

    for folder, files in structure.items():
        folder_path = os.path.join(project_name, folder)
        os.makedirs(folder_path, exist_ok=True)

        for file in files:
            file_path = os.path.join(folder_path, file)
            open(file_path, "w").close()
