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

        regexp_value = ('^()' if m.group(2) == '^^' else '(%s)' % re.escape(m.group(1))) + \
            '(.*?)' + \
            ('$' if m.group(3) == '$$' else '(%s)' % re.escape(m.group(4)))

        self.regex_pattern = RegExPattern(tracked_version, regexp_value)

    def apply_pattern(self, input_str: str) -> str:
        return self.regex_pattern.apply_pattern(input_str)

    def match_count(self) -> int:
        return self.regex_pattern.match_count
