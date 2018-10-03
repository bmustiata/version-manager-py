import subprocess
import re
from termcolor_util import eprint, red

DIVERGED_FROM_RELEASE = re.compile(r'.+?-\d+-\S+$')


def print_current_tag_version() -> None:
    current_release_version: str
    try:
        current_release_version = subprocess.check_output([
            "git", "describe"
        ]).decode('utf-8').strip()
    except Exception as e:
        eprint(red(str(e)))
        current_release_version = "1.0.0"

    if not DIVERGED_FROM_RELEASE.match(current_release_version):
        print(current_release_version)
        return  # => we're on a tagged release

    current_branch_name: str = subprocess.check_output([
        "git", "rev-parse", "--abbrev-ref", "HEAD"
    ]).decode('utf-8').strip()

    tag_name = f"{current_branch_name}"
    print(escape_tag_name(tag_name))


def escape_tag_name(name: str) -> str:
    return re.sub(r'[^A-Za-z-0-9]', '_', name)
