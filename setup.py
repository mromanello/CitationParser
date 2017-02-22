import os
from setuptools import setup, find_packages

NAME = "citation_parser"
execfile('{0}/__version__.py'.format(NAME))
VERSION = str_version

def read(fname):
   return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name=NAME,
	author='Matteo Romanello',
	author_email='matteo.romanello@gmail.com',
    license='GPL v3',
	url='https://github.com/mromanello/CitationParser',
    dependency_links=[
        'https://github.com/mromanello/pyCTS/tarball/master#egg=pyCTS-0.1.1'
        ,'http://www.antlr3.org/download/Python/antlr_python_runtime-3.1.3.tar.gz'
    ],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX'
    ],
    description='A parser for canonical references.',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    #package_data={'citation_parser': ['data/*.*']},
    long_description=read('README.rst'),
    install_requires=['pyCTS', 'antlr-python-runtime'],
    zip_safe=False,
)
