from distutils.core import setup
import py2exe

setup(
    console = ['mysqlimporter.py'],
    options = {
        "py2exe" : {
            "includes" : [],
            "bundle_files" : 1,
            "compressed" : True
        }
    },
    zipfile = None
)

#python basic_setup_mysqlimporter.py py2exe