import inquirer
from rich.console import Console

from .load_extension_groups import load_extension_groups
from .create_extensions_table import create_extensions_table

from .vscode.install_vscode_extensions import install_vscode_extension
from .vscode.list_installed_vscode_extensions import list_installed_vscode_extensions
from .vscode.uninstall_vscode_extensions import uninstall_vscode_extension
from .vscode.load_all_extension_details import load_all_extension_details

console = Console()


def apply_groups(profile: str):
    # Load all extension details
    all_extensions = load_all_extension_details()

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
    actions = 0
    if extensions_to_remove:
        create_extensions_table(
            list(extensions_to_remove),
            all_extensions,
            f"Extensions to remove in {profile}:",
        )
        to_remove = inquirer.confirm(
            message=f"Do you want to remove the following extensions in {profile}?",
            choices=extensions_to_remove,
        )
        if to_remove:
            for ext in extensions_to_remove:
                uninstall_vscode_extension(profile, ext)
            actions += 1
            console.print(
                f"Removed {len(extensions_to_remove)} extensions in {profile}"
            )
    if extensions_to_install:
        create_extensions_table(
            list(extensions_to_install),
            all_extensions,
            f"Extensions to install in {profile}:",
        )
        to_install = inquirer.confirm(
            message=f"Do you want to install the following extensions in {profile}?",
            choices=extensions_to_install,
        )
        if to_install:
            for ext in extensions_to_install:
                install_vscode_extension(profile, ext)
            actions += 1
            console.print(
                f"Installed {len(extensions_to_install)} extensions in {profile}"
            )

    if not actions:
        console.print("No actions performed.")
