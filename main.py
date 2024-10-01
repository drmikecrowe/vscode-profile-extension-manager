import rich
import click

from vem.apply_groups import apply_groups
from vem.update_extensions_from_profile import update_extensions_from_profile
from vem.categorize_extensions import categorize_extensions


@click.group()
def cli():
    pass


@cli.command(help="Extract extensions from VS Code profiles")
@click.option(
    "--profile",
    "-p",
    default=["Default"],
    help="Profile to export (can be used multiple times)",
    multiple=True,
)
def dump(profile):
    """
    Dump extensions from the specified profile(s).
    """
    for p in profile:
        update_extensions_from_profile(p)


@cli.command(help="Loop thru extensions categorizing them into groups")
@click.option(
    "--all",
    "-a",
    is_flag=True,
    help="Categorize all extensions (default is new extensions only)",
    default=False,
)
def categorize(all):
    categorize_extensions(uncategorized_only=not all)


@cli.command()
@click.option("--profile", "-p", default="Default", help="Profile to use")
def apply(profile):
    apply_groups(profile)
    pass


if __name__ == "__main__":
    cli()
