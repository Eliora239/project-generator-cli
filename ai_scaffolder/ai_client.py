import os


def call_llm(prompt: str) -> str:
    """
    Mocked LLM call.
    Replace this function with a real API call if needed.
    """
    return f"""# Project Documentation

This documentation was generated using an AI assistant (mocked).

## Prompt Used
{prompt}

## Description
This project was generated using The AI Scaffolder CLI.
"""


def generate_readme_from_structure(project_path: str) -> str:
    files = []

    for root, _, filenames in os.walk(project_path):
        for name in filenames:
            files.append(os.path.join(root, name))

    prompt = "Generate a professional README for a project with the following files:\n"
    prompt += "\n".join(files)

    return call_llm(prompt)
