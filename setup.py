import os
from subprocess import call
from glob import glob
from distutils.core import setup

# Screw the MANIFEST file, it just caches out of date data and messes
# up my builds.
mfst = os.path.join(os.path.dirname(__file__), "MANIFEST")
if os.path.exists(mfst):
    os.unlink(mfst)

# Compile translations.
call(['lrelease', 'lxdm-customizer.pro'])

translation_path = os.path.join('share', 'lxdm-customizer', 'translations')
DATA_FILES = [(translation_path,
              glob('i18n/*.qm')),]

setup(name='lxdm-customizer',
      version='1.0',
      description='LXDM customization tool',
      author='Yan-ren Tsai',
      author_email='elleryq@gmail.com',
      url='https://github.com/elleryq/lxdm-customizer',
      scripts=['lxdm-customizer.py'],
      packages=['lxdm_customizer_lib'],
      license="GPL2",
      data_files=DATA_FILES,
      )
