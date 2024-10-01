import inquirer
from vem.load_extension_groups import load_extension_groups

from rich.console import Console

from vem.vscode.list_installed_vscode_extensions import list_installed_vscode_extensions

console = Console()


def apply_groups(profile: str):
    # Load all extension groups
    all_groups = load_extension_groups()

    # Remove the 'removed' group if it exists
    groups = [group for group in all_groups if group not in ["Default", "removed"]]

    # Ask the user to select groups
    selected_groups = inquirer.checkbox(
        message=f"Select groups to apply to {profile}",
        choices=groups,
    )

    selected_groups.append("Default")

    current_extensions, err = list_installed_vscode_extensions(profile)
    if err:
        console.print(f"Error: {err}")
        return
    assert current_extensions
    desired_extensions = []
    for group in selected_groups:
        desired_extensions.extend(all_groups[group])

    extensions_to_install = set(desired_extensions) - set(current_extensions)
    extensions_to_remove = set(current_extensions) - set(desired_extensions)

    console.print(f"Extensions to install in {profile}:", extensions_to_install)
    console.print(f"Extensions to remove in {profile}:", extensions_to_remove)
