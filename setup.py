import os
from setuptools import setup, find_packages
import citation_parser

VERSION = citation_parser.__version__
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='CitationParser',
	author='Matteo Romanello',
	author_email='matteo.romanello@gmail.com',
	url='https://github.com/mromanello/CitationParser',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    #package_data={'citation_parser': ['data/*.*']},
    long_description=read('README.md'),
    #install_requires=['partitioner','CRFPP'],
    zip_safe=False,
)
