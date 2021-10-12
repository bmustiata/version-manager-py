python_binary(
  name="version-manager",
  main="version_manager/__main__.py",
  srcs=glob([
    "version_manager/**/*.py",
  ], exclude=[
    "version_manager/__main__.py",
  ]),
  deps=[
    "//_build/thirdparty/python:colorama",
    "//_build/thirdparty/python:PyYAML",

    "//tools/termcolor-util:termcolor-util-lib",
  ],
)
