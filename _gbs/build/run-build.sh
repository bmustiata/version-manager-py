# run static type checking
echo #############################################################################
echo # Static analysis
echo #############################################################################
mypy -m version_manager

# run the tests
python -m unittest version_manager.tests

# run the install of the package
python setup.py install

# create the single binary
pyinstaller version-manager.spec

