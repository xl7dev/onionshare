# -*- mode: python -*-
a = Analysis(['install/onionshare-launcher.py'],
    pathex=['.'],
    hiddenimports=['onionshare', 'onionshare_gui'],
    hookspath=None,
    runtime_hooks=None)
a.datas += [
    ('onionshare/index.html', 'onionshare/index.html', 'DATA'),
    ('onionshare/404.html', 'onionshare/404.html', 'DATA'),
    ('images/logo.png', 'images/logo.png', 'DATA'),
    ('images/drop_files.png', 'images/drop_files.png', 'DATA'),
    ('images/server_stopped.png', 'images/server_stopped.png', 'DATA'),
    ('images/server_started.png', 'images/server_started.png', 'DATA'),
    ('images/server_working.png', 'images/server_working.png', 'DATA'),
    ('locale/de.json', 'locale/de.json', 'DATA'),
    ('locale/en.json', 'locale/en.json', 'DATA'),
    ('locale/es.json', 'locale/es.json', 'DATA'),
    ('locale/fi.json', 'locale/fi.json', 'DATA'),
    ('locale/fr.json', 'locale/fr.json', 'DATA'),
    ('locale/it.json', 'locale/it.json', 'DATA'),
    ('locale/nl.json', 'locale/nl.json', 'DATA'),
    ('locale/no.json', 'locale/no.json', 'DATA'),
    ('locale/pt.json', 'locale/pt.json', 'DATA'),
    ('locale/ru.json', 'locale/ru.json', 'DATA'),
    ('locale/tr.json', 'locale/tr.json', 'DATA'),
]
pyz = PYZ(a.pure)
exe = EXE(pyz,
    a.scripts,
    exclude_binaries=True,
    name='onionshare-launcher',
    debug=False,
    strip=False,
    upx=True,
    console=False )
coll = COLLECT(exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='onionshare')
app = BUNDLE(exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='OnionShare.app',
    appname='OnionShare',
    icon='install/onionshare.icns',
    version=open('version').read().strip())