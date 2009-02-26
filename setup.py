from distutils.core import setup
from distutils.command.install_data import install_data
from distutils.extension import Extension

from Cython.Distutils import build_ext

# Uncomment this line if you are building for windows
#import py2exe

class smart_install_data(install_data):
    def run(self):
        #need to change self.install_dir to the library dir
        install_dir = self.get_finalized_command("install")
        self.install_dir = getattr(install_cmd, "install_lib")
        return install_data.run(self)

pydft = Extension("wonderful.pydft", 
                  sources=["wonderful/pydft.pyx", "wonderful/dft.c"])
wonderful = Extension("wonderful.wonderful",
                      sources=["wonderful/wonderful.pyx", 
                               "wonderful/dft.c", 
                               "wonderful/c_wonderful.c"],
                      libraries=["portaudio"])

setup(
  name = 'bosseonfire',
  version='0.1',
  description="Guitar game using Fourier Transforms",
  author="Jonne Mickelin, Jakob Florell",
  url="http://guitarlegend.googlecode.com",
  license="GPL v3",
  packages=["", "wonderful"],

  windows=["main.py"],
  options={"py2exe": {"compressed": 1,
                       },
			},
  
  ext_modules=[pydft, wonderful],
  cmdclass = {'build_ext': build_ext,
              #'install_data': smart_install_data,
              },
  data_files=[("", ["avbin.dll"])]
)
