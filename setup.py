from setuptools import setup, find_packages

setup(
    name='albertus-djangus',
    version='0.1dev',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    url='git@github.com:livengooddaily/albertus-djangus.git',
    author='Eddie Livengood',
    author_email='eddie.livengood@gmail.com',
    install_requires=['Pillow','wiki'],
    packages=find_packages()
)