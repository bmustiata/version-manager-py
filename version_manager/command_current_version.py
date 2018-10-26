import subprocess
import re
from termcolor_util import eprint, red

DIVERGED_FROM_RELEASE = re.compile(r'.+?-\d+-\S+$')


def print_current_tag_version(default_branch_name: str) -> None:
    current_release_version: str
    try:
        current_release_version = subprocess.check_output([
            "git", "describe"
        ]).decode('utf-8').strip()

        if not DIVERGED_FROM_RELEASE.match(current_release_version):
            print(current_release_version)
            return  # => we're on a tagged release
    except Exception as e:
        eprint(red(str(e)))

    current_branch_name: str = subprocess.check_output([
        "git", "rev-parse", "--abbrev-ref", "HEAD"
    ]).decode('utf-8').strip()

    tag_name = current_branch_name if current_branch_name != "HEAD" else default_branch_name
    print(f"0.1.{escape_tag_name(tag_name)}")


def escape_tag_name(name: str) -> str:
    return re.sub(r'[^A-Za-z-0-9]', '_', name)
