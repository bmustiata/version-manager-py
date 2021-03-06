import germanium_py_exe  # type: ignore


germanium_py_exe.pipeline(
    {
        "repo": "git@github.com:bmustiata/version-manager-py.git",
        "run_black": False,
        "run_flake8": False,
        "run_version_manager": False,
        "binaries": {
            "name": "Python 3.8 on Linux x64",
            "platform": "python:3.8",
            "publish_pypi": "sdist",
        },
    }
)
