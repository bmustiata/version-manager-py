import termcolor
import sys


def eprint(*args) -> None:
    print(*args, file=sys.stderr)


def red(s: str) -> str:
    return termcolor.colored(s, 'red')


def yellow(s: str) -> str:
    return termcolor.colored(s, 'yellow')


def green(s: str) -> str:
    return termcolor.colored(s, 'green')


def cyan(s: str) -> str:
    return termcolor.colored(s, 'cyan')
