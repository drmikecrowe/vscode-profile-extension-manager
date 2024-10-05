from appdirs import user_config_dir
import os

CONFIG_DIR = user_config_dir("vpem")
if not os.path.exists(CONFIG_DIR):
    os.makedirs(CONFIG_DIR)

ALL_EXTENSION_DETAILS = os.path.join(CONFIG_DIR, "vscode-extensions-with-desc.json")
EXTENSION_GROUPS = os.path.join(CONFIG_DIR, "vscode-extensions-groups.json")
