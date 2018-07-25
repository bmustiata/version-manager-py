import subprocess
import re
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

    tag_name = f"{current_release_version}-{current_branch_name}"
    print(escape_tag_name(tag_name))


def escape_tag_name(name: str) -> str:
    return re.sub(r'[^A-Za-z-0-9]', '_', name)
