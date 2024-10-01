import click
import json
import subprocess
from pathlib import Path


def manage_extensions(profile):
    # List groups in singles and create a select
    singles_dir = Path("singles")
    groups = [f.stem for f in singles_dir.glob("*.json") if f.stem != "default"]
    selected_groups = click.prompt(
        "Select groups (comma-separated)", type=click.STRING, default=",".join(groups)
    ).split(",")

    # Dump the list of currently installed extensions
    result = subprocess.run(
        ["code", "--profile", profile, "--list-extensions"],
        capture_output=True,
        text=True,
    )
    installed = set(result.stdout.strip().split("\n"))

    # Combine keys from default.json and selected groups
    combined_extensions = set()
    with open(singles_dir / "default.json", "r") as f:
        combined_extensions.update(json.load(f).keys())

    for group in selected_groups:
        with open(singles_dir / f"{group}.json", "r") as f:
            combined_extensions.update(json.load(f).keys())

    # Identify missing and extra keys
    missing_extensions = combined_extensions - installed
    extra_extensions = installed - combined_extensions

    # Print results
    click.echo(f"\nProfile: {profile}")
    click.echo(f"Selected groups: {', '.join(selected_groups)}")
    click.echo(f"\nMissing extensions:")
    for ext in sorted(missing_extensions):
        click.echo(f"  {ext}")
    click.echo(f"\nExtra extensions:")
    for ext in sorted(extra_extensions):
        click.echo(f"  {ext}")


if __name__ == "__main__":
    manage_extensions("Default")
