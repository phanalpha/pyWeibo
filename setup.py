from setuptools import setup, find_packages

setup(
    name="pyWeibo",
    version="0.1.0",
    packages=find_packages(),
    namespace_packages=['picoriver'],
    install_requires=['enum34']
)
