#from distutils.core import setup
from setuptools import setup
import os

def read(filename):
    return file(filename).read()

setup(
    name='diagram',
    version='0.2.21.1',
    description='Text mode diagrams using UTF-8 characters and fancy colors',
    long_description=read('README.txt'),
    url='https://github.com/tehmaze/diagram',
    author='Wijnand Modderman-Lenstra',
    author_email='maze@pyth0n.org',
    keywords=['diagram', 'graph', 'ascii', 'ansi', 'text'],
    py_modules=['diagram'],
    scripts=[os.path.join('bin', 'diagram')],
)
