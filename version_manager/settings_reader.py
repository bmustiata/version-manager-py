import sys
from os import path
from typing import Dict, Optional

import yaml
from termcolor_util import red

from .custom.custom_pattern_definition import CustomPatternDefinition
from .custom.custom_settings import ExtraSettings
from .matcher_builder import matcher_builder
from .matchers.pattern import TrackedVersionSet, TrackedVersion


def read_settings_file(
    settings_file: str,
    override_settings: Dict[str, str],
    ignore_missing_parents: bool,
    cwd: str,
    display_item: Optional[str] = None,
) -> TrackedVersionSet:
    """
    Read the configured versions from the files. If a version is defined in the
    override_settings, then that value is going to be used, instead of what's
    read from the file.

    This allows overwriting versions, regardless of where they're read from.
    """
    if not path.exists(settings_file):
        settings_file = path.join(path.dirname(settings_file), "versions.yml")

        if not path.exists(settings_file):
            report_missing_settings_file(settings_file)
            sys.exit(1)

    with open(settings_file, "r", encoding="utf-8") as stream:
        settings_items = list(yaml.safe_load_all(stream))

    tracked_entries = read_tracked_entries(settings_items)
    extra_settings = read_extra_settings(settings_items)

    result = list()

    for name, tracked_entry in tracked_entries.items():
        if display_item and name != display_item:
            continue

        try:
            tracked_version: TrackedVersion = TrackedVersion(name)
            tracked_version.version = (
                override_settings[name]
                if name in override_settings
                else parse_version(
                    tracked_entry["version"],
                    override_settings,
                    ignore_missing_parents,
                    cwd=cwd,
                )
            )

            tracked_files = tracked_entry["files"] if "files" in tracked_entry else {}

            for file_name in tracked_files.keys():
                tracked_file = matcher_builder(
                    tracked_version=tracked_version,
                    file_item=tracked_files[file_name],
                    extra_settings=extra_settings,
                )
                tracked_version.files[file_name] = tracked_file
        except ParentNotFound as e:
            if ignore_missing_parents:
                continue

            raise Exception("Unable to find parent", e)
        except Exception as e:
            raise Exception("Unable to read value: %s" % name, e)
        else:
            result.append(tracked_version)

    return result


def read_extra_settings(settings_items):
    if len(settings_items) <= 1:
        return ExtraSettings()

    result = ExtraSettings()

    extra_settings_dict = settings_items[0]

    if "custom" not in extra_settings_dict:
        raise Exception("Missing `custom` definition for expressions")

    for k, v in extra_settings_dict["custom"].items():
        result.custom_pattern_definitions[k] = CustomPatternDefinition(name=k, regex=v)

    return result



def read_tracked_entries(settings_items):
    return settings_items[len(settings_items) - 1]


def report_missing_settings_file(settings_file: str) -> None:
    print(red("%s configuration file is missing." % settings_file))


# This import is intentionally at the end, because it's a cyclic import
from .parse_version import parse_version, ParentNotFound  # NOQA
