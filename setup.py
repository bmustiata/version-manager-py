from setuptools import setup
from setuptools import find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

packages = find_packages()

setup(
    name='vm',
    version='2.0.17',
    description='version_manager',
    long_description=readme,
    author='Bogdan Mustiata',
    author_email='bogdan.mustiata@gmail.com',
    license='BSD',
    entry_points={
        "console_scripts": [
            "version-manager=version_manager.mainapp:main",
            "vm=version_manager.mainapp:main"
        ]
    },
    install_requires=[
        "colorama==0.3.7",
        "termcolor==1.1.0",
        "termcolor_util==1.0.1",
        "PyYAML==3.12"],
    packages=packages,
    package_data={
        '': ['*.txt', '*.rst']
    })
