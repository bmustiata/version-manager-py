from abc import ABCMeta, abstractmethod
from typing import Dict, List


class Pattern(metaclass=ABCMeta):
    tracked_version: "TrackedVersion"

    @abstractmethod
    def apply_pattern(self, input: str) -> str:
        pass

    @property
    @abstractmethod
    def match_count(self) -> int:
        pass

    @property
    @abstractmethod
    def expected_count(self) -> int:
        pass


class TrackedVersion:
    name: str
    version: str
    files: Dict[str, Pattern]

    def __init__(self, name: str) -> None:
        self.name = name
        self.version = ""
        self.files = dict()


TrackedVersionSet = List[TrackedVersion]
