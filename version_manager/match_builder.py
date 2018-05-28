from typing import Any

from matchers.pattern import TrackedVersion, Pattern
from matchers.array_pattern import ArrayPattern
from matchers.regex_pattern import RegExPattern


def matcher_builder(tracked_version: TrackedVersion,
                  file_item: Any) -> Pattern:
    if isinstance(file_item, list):
        file_items = map(lambda it: matcher_builder(tracked_version, it),
                         file_item)

        return ArrayPattern(tracked_version, file_items)

    return RegExPattern(tracked_version, file_item)
