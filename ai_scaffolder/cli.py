import click
from ai_scaffolder.scaffolder import generate_project
from ai_scaffolder.vibe import run_vibe
from ai_scaffolder.ai_client import generate_readme_from_structure


@click.group()
def cli():
    """The AI Scaffolder CLI"""
    pass


@cli.command()
@click.argument("template_path")
def scaffold(template_path):
    """
    Generate a project structure from a template.json file.
    """
    generate_project(template_path)
    click.echo("✅ Project structure generated successfully.")


@cli.command()
@click.argument("project_path")
def readme(project_path):
    """
    Generate a README.md using AI (mocked).
    """
    content = generate_readme_from_structure(project_path)

    with open(f"{project_path}/README.md", "w", encoding="utf-8") as f:
        f.write(content)

    click.echo(" README.md generated successfully.")


@cli.command()
@click.argument("instructions")
@click.option("--in", "inputs", multiple=True, required=True)
@click.option("--out", "output", required=True)
def vibe(instructions, inputs, output):
    """
    Apply AI transformation to input files using instructions.
    """
    run_vibe(instructions, inputs, output)
    click.echo(" Vibe processing completed.")


if __name__ == "__main__":
    cli()
