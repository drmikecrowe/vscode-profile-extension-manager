import click
from vem.update_extensions_from_profile import update_extensions_from_profile


@click.command()
@click.argument("profiles", nargs=-1, required=True)
def dump_extensions(profiles):
    """
    Dump extensions from the specified profile(s).
    """
    for profile in profiles:
        update_extensions_from_profile(profile)
