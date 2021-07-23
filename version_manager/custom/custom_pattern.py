from version_manager.matchers.pattern import TrackedVersion
from version_manager.matchers.regex_pattern import RegExPattern


class CustomPattern(RegExPattern):
    def __init__(self,
                 name: str,
                 tracked_version: TrackedVersion,
                 expression: str) -> None:
        super(CustomPattern, self).__init__(
            tracked_version=tracked_version,
            expression=expression,
        )

        self.name = name
