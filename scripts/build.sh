#!/usr/bin/env bash

pyinstaller vpem.py --name vpem \
    --onefile \
    --hidden-import vpem \
    --hidden-import inquirer \
    --hidden-import rich \
    --hidden-import rich.progress \
    --hidden-import rich.prompt \
    --hidden-import rich.console \
    --hidden-import click \
    --hidden-import prodict \
    --hidden-import requests \
    --copy-metadata readchar \
    --add-data "vpem:vpem" \
    --log-level WARN