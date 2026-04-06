# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['Principal.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('fondo.jpg', '.'),     # Fondo
        ('iconom.ico', '.')     # Icono
        # ❌ Se quitó MANTENIMIENTO.db
    ],
    hiddenimports=[
        'tkcalendar',
        'win32timezone',
        'babel.numbers'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Principal',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='iconom.ico'
)
