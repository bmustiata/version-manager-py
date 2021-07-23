from typing import Dict

from version_manager.custom.custom_pattern_definition import CustomPatternDefinition


class ExtraSettings:
    def __init__(self) -> None:
        self.custom_pattern_definitions: Dict[str, CustomPatternDefinition] = dict()
