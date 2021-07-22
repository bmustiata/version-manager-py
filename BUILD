python_binary(
  name="version-manager",
  main="version_manager/__main__.py",
  srcs=glob([
    "version_manager/**/*.py",
  ], exclude=[
    "version_manager/__main__.py",
  ]),
  deps=[
    "//build/thirdparty/python:colorama",
    "//build/thirdparty/python:PyYAML",

    # FIXME: this should be used after https://github.com/thought-machine/please/pull/1912 is merged
    "//tools/termcolor-util:termcolor-util-lib",
  ],
)
