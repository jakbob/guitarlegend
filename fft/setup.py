from distutils.core import setup
from distutils.extension import Extension

setup(
    name='fft',
    ext_modules = [Extension("pydft", ["pydft.c","dft.c"])]
)
