from setuptools import setup, Extension

#  https://stackoverflow.com/questions/4529555/building-a-ctypes-based-c-library-with-distutils
from distutils.command.build_ext import build_ext as build_ext_orig


class CTypesExtension(Extension):
    pass


class build_ext(build_ext_orig):
    def build_extension(self, ext):
        self._ctypes = isinstance(ext, CTypesExtension)
        return super().build_extension(ext)

    def get_export_symbols(self, ext):
        if self._ctypes:
            return ext.export_symbols
        return super().get_export_symbols(ext)

    def get_ext_filename(self, ext_name):
        if self._ctypes:
            return ext_name + ".so"
        return super().get_ext_filename(ext_name)


setup(
    py_modules=["ctypesexample.summing"],
    ext_modules=[
        CTypesExtension(
            "ctypesexample.csumlib",
            ["ctypesexample/csumlib.cpp"],
            extra_compile_args=['-fopenmp'],
            extra_link_args=['-lgomp'],
        ),
    ],
    cmdclass={"build_ext": build_ext},
)
