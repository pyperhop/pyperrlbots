# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['C:\\Users\\pyper\\Desktop\\pyper-rl-bots'],  # Setze hier den Pfad zu deinem Projekt
    binaries=[],
    datas=[('C:\\Users\\pyper\\Desktop\\pyper-rl-bots\\logo.ico', '.')],  # Füge das Icon hier hinzu
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
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
    icon='C:\\Users\\pyper\\Desktop\\pyper-rl-bots\\logo.ico',  # Setze hier den Pfad zum Icon
)
