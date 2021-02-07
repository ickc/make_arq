from distutils.core import setup, Extension
import numpy

setup(
    name="_makearq",
    version="0.1",
    description="make_arq helper",
    ext_modules=[
        Extension("_makearq", ["src/make_arq/_makearq.c"], include_dirs=[numpy.get_include()])
    ],
)
