"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

# Config section, change this for each release
GCC_DIR='gcc'

#Do not change anything below here
APP = ['run-mbed-cli.py']
APP_NAME = "MBED_CLI"
DATA_FILES = ['run-mbed-cli.sh',GCC_DIR,"bin","git"]
OPTIONS = {
    'argv_emulation': True,
    'iconfile': './mbed-cli-logo.icns',
    'packages':['mbed','mbed_lstools','mbed_greentea','mbed_host_tests',"serial","bs4","jinja2","elftools","fuzzywuzzy","mercurial","hgdemandimport","hgext","hgext3rd"],
    # 'includes': "mbed,mbed_lstools,mbed_greentea,mbed_host_tests",
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "Run MBED CLI",
        'CFBundleIdentifier': "com.armmbed.osx.mbed-cli",
        'CFBundleVersion': "0.0.1",
        'CFBundleShortVersionString': "0.0.1",
        'NSHumanReadableCopyright': u"Copyright 2018 arm MBED All Rights Reserved",
        'CFBundleIconFile':'mbed-cli-logo.icns'
    }
}


setup(
	name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
