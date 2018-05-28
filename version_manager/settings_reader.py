from typing import Dict, List
import yaml
import sys
from os import path

from parse_version import parse_version
from match_builder import match_builder
from interfaces import TrackedVersionSet, TrackedVersion


def read_settings_file(settings_file: str,
                       override_settings: Dict[str, str]) -> TrackedVersionSet:
    if not path.exists(settings_file):
        settings_file = path.join(path.dirname(settings_file), 'versions.yml')

        if not path.exists(settings_file):
            report_missing_settings_file(settings_file)
            sys.exit(1)

    with open(settings_file, encoding='utf-8') as stream:
        settings = yaml.load(stream)

    result = TrackedVersionSet()

    for name, tracked_entry in settings.items():
        tracked_version: TrackedVersion = TrackedVersion(name)
        tracked_version.version = override_settings[name] if \
                                  tracked_version.name in override_settings else \
                                  parse_version(tracked_version.version, override_settings)

        tracked_files = tracked_entry.files if tracked_entry.files else {}

        for file_name in tracked_files.keys():
            tracked_version.files[file_name] = match_builder(tracked_version,
                                                             tracked_files[file_name])

        result.append(tracked_version)

    return result


def report_missing_settings_file(settings_file: str) -> None:
    print("config missing")
