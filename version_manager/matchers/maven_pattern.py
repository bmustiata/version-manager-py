import re

from .pattern import Pattern, TrackedVersion
from .regex_pattern import RegExPattern


class MavenPattern(Pattern):
    RE = re.compile(r'^maven\:(.*?)\:(.*?)$')

    def __init__(self,
                 tracked_version: TrackedVersion,
                 expression: str) -> None:
        m = MavenPattern.RE.match(expression)

        regexp_value = "(<groupId>%s</groupId>\\s*"\
                       "<artifactId>%s</artifactId>\\s*"\
                       "<version>)(.*?)(</version>)" % \
                       (re.escape(m.group(1)), re.escape(m.group(2)))

        self.regex_pattern = RegExPattern(tracked_version, regexp_value)

    def apply_pattern(self, input: str) -> str:
        return self.regex_pattern.apply_pattern(input)

    def match_count(self) -> int:
        return self.regex_pattern.match_count

    def expected_count(self) -> int:
        return self.regex_pattern.expected_count