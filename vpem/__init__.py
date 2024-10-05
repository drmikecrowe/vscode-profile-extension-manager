from appdirs import user_config_dir
import os

config_dir = user_config_dir("vpem")
if not os.path.exists(config_dir):
    os.makedirs(config_dir)

ALL_EXTENSION_DETAILS = os.path.join(config_dir, "vscode-extensions-with-desc.json")
EXTENSION_GROUPS = os.path.join(config_dir, "vscode-extensions-groups.json")
