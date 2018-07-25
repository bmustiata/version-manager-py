import subprocess
from termcolor_util import eprint, red


def print_current_tag_version() -> None:
    current_branch_name: str = subprocess.check_output([
        "git", "rev-parse", "--abbrev-ref", "HEAD"
        ]).decode('utf-8').strip()

    current_release_version: str
    try:
        current_release_version = subprocess.check_output([
            "git", "describe"
            ]).decode('utf-8').strip()
    except Exception as e:
        eprint(red(str(e)))
        current_release_version = "1.0.0"

    print(f"{current_release_version}-{current_branch_name}")
