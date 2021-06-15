import subprocess
import re
import os
from termcolor_util import eprint, red

DIVERGED_FROM_RELEASE = re.compile(r"^.+?-\d+-\S+$")


def print_current_tag_version() -> None:
    version_name = get_current_tag_version()
    print(version_name)


def get_current_tag_version() -> str:
    # If we have the VERSION_MANAGER_TAG in the environment,
    # we use it instead of whatever git tag, or derived name
    # from the branch.
    if "VERSION_MANAGER_TAG" in os.environ:
        return os.environ["VERSION_MANAGER_TAG"]

    # if we have BRANCH_NAME in the environment, we use that one,
    # since it's already found for us.
    if "BRANCH_NAME" in os.environ:
        env_branch_name = os.environ["BRANCH_NAME"]

        if "/" not in env_branch_name:
            return env_branch_name

        return f"0.0.0-{escape_tag_name(env_branch_name)}"

    # We try to find if we have an annotated git tag
    try:
        current_release_version: str = subprocess.check_output(
            ["git", "describe"]
        ).decode("utf-8").strip()

        if not DIVERGED_FROM_RELEASE.match(current_release_version):
            return current_release_version  # => we're on a tagged release
    except Exception as e:
        eprint(red(str(e)))

    # We try to find the current branch name
    current_branch_name: str = subprocess.check_output(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"]
    ).decode("utf-8").strip()

    return f"0.0.0-{escape_tag_name(current_branch_name)}"


def escape_tag_name(name: str) -> str:
    return re.sub(r"[^A-Za-z-0-9]", "-", name)
