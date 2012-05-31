from distutils.core import setup
import os, sys, glob

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name="quickedit",
      scripts=['quickedit'],
      version='0.99.9',
      maintainer="Ricardo Band",
      maintainer_email="quickedit@xengi.de",
      description="Change your Quick-launch icons easily.",
      long_description=read('quickedit.longdesc'),
      data_files=[('share/applications',['quickedit.desktop']),
                  ('share/icons/hicolor/64x64/apps', ['quickedit.png']),
                  ('/opt/quickedit/qml', glob.glob('qml/*.qml')), ],)
