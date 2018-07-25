from setuptools import setup
from setuptools import find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()  # type: str
    install_requires = list(filter(
        lambda it: it,
        requirements.splitlines()))


setup(
    name='vm',
    version='2.0.5',
    entry_points={
        "console_scripts": [
            "version-manager = version_manager.launcher:launch",
            "vm = version_manager.launcher:launch",
        ]
    },
    description='vm: version manager',
    long_description=readme,
    author='Bogdan Mustiata',
    author_email='bogdan.mustiata@gmail.com',
    license='BSD',
    install_requires=install_requires,
    packages=packages
)

