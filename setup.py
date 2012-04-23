from distutils.core import setup
import os, sys, glob

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name="quickedit",
      scripts=['quickedit'],
      version='0.2.0',
      maintainer="Ricardo Band",
      maintainer_email="quickedit@makesyouhappy.org",
      description="Change your Quick-launch icons easily.",
      long_description=read('quickedit.longdesc'),
      data_files=[('share/applications',['quickedit.desktop']),
                  ('share/icons/hicolor/64x64/apps', ['quickedit.png']),
                  ('share/quickedit/qml', glob.glob('qml/*.qml')), ],)
