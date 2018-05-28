from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='version-manager',
    version='1.0.0',
    description='version-manager',
    long_description = readme,
    author='Bogdan Mustiata',
    author_email='bogdan.mustiata@gmail.com',
    license='BSD',
    install_requires=['wut'],
    packages=['version_manager'])
