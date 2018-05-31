# -*- mode: python -*-
import os.path


print("Current dir is: %s" % os.path.curdir)


block_cipher = None

a = Analysis(['version_manager/launcher.py'],
             pathex=[os.path.curdir],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='version-manager',
          debug=True,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=True )
