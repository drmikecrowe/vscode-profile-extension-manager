# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import copy_metadata

datas = [('vpem', 'vpem')]
datas += copy_metadata('readchar')


a = Analysis(
    ['vpem.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=['vpem', 'inquirer', 'rich', 'rich.progress', 'rich.prompt', 'rich.console', 'click', 'prodict', 'requests', 'appdirs'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='vpem',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
