from distutils.core import setup
import py2exe
import sys
import glob

msvc = 'Microsoft.VC90.CRT'
conf_files = ['config.json']
ext_units = ['Tkinter', 'unittest', 'email', 'logging']

setup(
    service = [
        {
            'modules' : 'svcmain',
            'icon_resources' : [(0, 'factory.ico'), ],
            },
        ],
    data_files = [('', conf_files),
                  (msvc, glob.glob(msvc + '/*.*'))],
    options = {
        'py2exe' : {
            'bundle_files' : '1',
            'excludes' : ext_units,
            }
        },
    zipfile = None,
    )
