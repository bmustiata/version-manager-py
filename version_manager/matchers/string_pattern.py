import re

from .pattern import Pattern, TrackedVersion
from .regex_pattern import RegExPattern


class StringPattern(Pattern):
    RE = re.compile(r'^(.*?)(\^\^|##|\*\*)VERSION(##|\*\*|\$\$)(.*?)$')

    def __init__(self,
                 tracked_version: TrackedVersion,
                 expression: str) -> None:
        m = StringPattern.RE.match(expression)

        if m.group(2) == '##' or m.group(3) == '#':
            print('old ver')

        regexp_value = ('^()' if m.group(2) == '^^' else '(%s)' % escape_string_regexp(m.group(1))) + \
                        '(.*?)' + \
                        ('$' if m.group(3) == '$$' else '(%s)' % escape_string_regexp(m.group(4)))

        self.regex_pattern = RegExPattern(tracked_version, regexp_value)


def escape_string_regexp(s: str) -> str:
    pass
