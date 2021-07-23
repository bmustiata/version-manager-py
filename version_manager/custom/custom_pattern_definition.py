import re

from version_manager.custom.custom_pattern import CustomPattern
from version_manager.matchers.pattern import TrackedVersion


class CustomPatternDefinition:
    def __init__(self,
                 name: str,
                 regex: str,
                 ) -> None:
        self.name = name
        self.regex_expression = regex

    def match(self, file_item: str) -> bool:
        if file_item.startswith(f"{self.name}:"):
            return True

    def create(self,
               tracked_version: TrackedVersion,
               expression: str) -> CustomPattern:
        static_values = expression.split(":")
        expression = self.regex_expression

        for i in reversed(range(1, len(static_values))):
            expression = expression.replace(f"${i}", re.escape(static_values[i]))

        expression = "(" + expression.replace("$value", ")(.+?)(") + ")"

        return CustomPattern(
            name=self.name,
            tracked_version=tracked_version,
            expression=expression,
        )
