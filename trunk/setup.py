from distutils.core import setup
from distutils.command.install_data import install_data
from distutils.extension import Extension
from Pyrex.Distutils import build_ext

class smart_install_data(install_data):
    def run(self):
        #need to change self.install_dir to the library dir
        install_dir = self.get_finalized_command("install")
        self.install_dir = getattr(install_cmd, "install_lib")
        return install_data.run(self)

setup(
  name = 'bosseonfire',
  version='0.1',
  description="Guitar game using Fourier Transforms",
  author="Jonne Mickelin, Jakob Florell",
  url="http://guitarlegend.googlecode.com",
  license="GPL v3",
  packages=["", "fft"],
  ext_modules=[ 
    Extension("wonderful.pydft",    ["wonderful/pydft.pyx", "wonderful/dft.c"]),
    Extension("wonderful",          ["wonderful/wonderful.pyx", "wonderful/dft.c", 
                                     "wonderful/wonderful.c"]),
    ],
  cmdclass = {'build_ext': build_ext,
              'install_data': smart_install_data,
              }
)
