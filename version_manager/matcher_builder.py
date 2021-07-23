from typing import Any

from .custom.custom_settings import ExtraSettings

from .matchers.pattern import TrackedVersion, Pattern
from .matchers.array_pattern import ArrayPattern
from .matchers.regex_pattern import RegExPattern
from .matchers.match_counter import MatchCounter
from .matchers.maven_pattern import MavenPattern
from .matchers.string_pattern import StringPattern


def matcher_builder(tracked_version: TrackedVersion,
                    file_item: Any,
                    extra_settings: ExtraSettings) -> Pattern:
    if isinstance(file_item, list):
        file_items = map(lambda it: matcher_builder(tracked_version, it), file_item)

        return ArrayPattern(tracked_version, list(file_items))

    if "count" in file_item:
        expression = (
            file_item["match"] if "match" in file_item else file_item["expression"]
        )

        return MatchCounter(
            tracked_version,
            matcher_builder(tracked_version, expression),
            int(file_item["count"]),
        )

    for _, custom_pattern_definition in extra_settings.custom_pattern_definitions.items():
        if custom_pattern_definition.match(file_item):
            return custom_pattern_definition.create(tracked_version, file_item)

    if MavenPattern.RE.match(file_item):
        return MavenPattern(tracked_version, file_item)

    if StringPattern.RE.match(file_item):
        return StringPattern(tracked_version, file_item)

    return RegExPattern(tracked_version, file_item)
