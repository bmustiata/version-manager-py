from setuptools import setup
from setuptools import find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

packages = find_packages()

setup(
    name='version_manager',
    version='2.0.15',
    description='version_manager',
    long_description=readme,
    author='Bogdan Mustiata',
    author_email='bogdan.mustiata@gmail.com',
    license='BSD',
    entry_points={
        "console_scripts": [
            "version-manager = application:launch",
            "vm = application:launch"
        ]
    },
    install_requires=[],
    packages=packages,
    package_data={
        '': ['*.txt', '*.rst']
    })
