#!/bin/env python3
""" setup.py """

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import os
import numpy

setup(cmdclass = {'build_ext': build_ext},
      name="alphapose.utils",
      version='1.0',
      ext_modules=[Extension("alphapose.utils.bbox", ["bbox_.py"]),
                   Extension("alphapose.utils.transforms", ["transforms_.py"]),
                   Extension("alphapose.utils.presets", ["./presets_/simple_transform.py"]),
                  ],
      package_dir={"alphapose.utils.presets.SimpleTransform": "./presets_/simple_transform.py"},
      include_dirs=[numpy.get_include(),
                    os.path.join(numpy.get_include(), 'numpy')]
      )
