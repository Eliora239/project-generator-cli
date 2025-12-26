from ai_scaffolder.ai_client import call_llm


def run_vibe(instructions_path: str, input_files: list, output_file: str):
    with open(instructions_path, "r", encoding="utf-8") as f:
        instructions = f.read()

    combined_content = ""

    for file_path in input_files:
        with open(file_path, "r", encoding="utf-8") as f:
            combined_content += f"\n--- {file_path} ---\n"
            combined_content += f.read()

    prompt = f"""
Instructions:
{instructions}

Files content:
{combined_content}
"""

    result = call_llm(prompt)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result)
