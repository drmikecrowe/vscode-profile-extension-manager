#!/usr/bin/env python
import sys
import click
import rich

from vpem.apply_groups import apply_groups
from vpem.categorize_extensions import categorize_extensions
from vpem.update_extensions_from_profile import update_extensions_from_profile


cmd = sys.argv[0]


@click.group()
def cli():
    pass


@cli.command(
    help="Extract extensions from VS Code profiles. Default profile always dumped. Add other profiles to the list."
)
@click.argument("profiles", nargs=-1)
def dump(profiles):
    """
    Dump extensions from the specified profile(s).
    """
    profiles = list(profiles)
    if "Default" not in profiles:
        profiles.insert(0, "Default")
    rich.print("Dumping profiles: " + ", ".join(profiles))
    for profile in profiles:
        update_extensions_from_profile(profile)
    rich.print(
        f"""
Now, categorize your apps:
$ {cmd} categorize
               """
    )


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
    rich.print(
        f"""
Now, initialize each profile separately by doing:
$ {cmd} apply Default
$ {cmd} apply Example                                             
               """
    )


@cli.command(help="Select groups defining your needs and apply to the VSCode profile")
@click.argument("profile", required=True)
def apply(profile):
    if not profile:
        raise ValueError("Profile name is required")
    apply_groups(profile)


if __name__ == "__main__":
    cli()
