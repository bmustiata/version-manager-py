# -*- mode: python -*-

block_cipher = None


a = Analysis(['version_manager/launcher.py'],
             pathex=['/home/raptor/projects/version-manager-py'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['pycrypto', 'PyInstaller', 'bz2'],
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
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
