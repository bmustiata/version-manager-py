from typing import Dict
import os
import subprocess
import re
from os import path

from interfaces import TrackedVersionSet
from util_find import find
from settings_reader import read_settings_file


setting_files: Dict[str, TrackedVersionSet] = dict()


def parse_parent_path(version: str,
                      cwd: str,
                      overriden_settings: Dict[str, str]) -> str:
    items = re.compile(r'^parent:(.+)@(.+?)$').match(version)

    if not items:
        raise Exception("The version must be in the 'parent:path@propertyname' "
                        "format, got instead: '%s'." % version)

    parent_versions_file_path = items.group(1)
    property_name = items.group(2)

    full_path = path.realpath(path.join(cwd, parent_versions_file_path))

    if not path.exists(full_path):
        raise Exception('Unable to find referenced file: %s' % full_path)

    if path.isdir(full_path):
        full_path = path.join(full_path, 'versions.json')

    if full_path not in setting_files:
        setting_files[full_path] = read_settings_file(full_path, overriden_settings)

    property_value = find(lambda it: it.name == property_name,
                          setting_files[full_path])

    if not property_value:
        available_properties = ", ".join(map(lambda it: "%s@%s" % (it.name, it.version),
                                             setting_files[full_path]))

        raise Exception("Property '%s' is not defined in %s settings file. "
                        "Available properties are: %s" % (
                            property_name,
                            full_path,
                            available_properties))

    return property_value.version


def parse_version_with_path(version: str,
                            cwd: str,
                            overriden_settings: Dict[str, str]) -> str:
    old_path = os.getcwd()

    if not isinstance(version, str):
        raise Exception("Got version a %s of type %s, in %s" % (
                        version,
                        type(version),
                        cwd))

    try:
        os.chdir(cwd)

        if version.startswith('parent:'):
            return parse_parent_path(version, cwd, overriden_settings)

        if '`' not in version and '$' not in version:
            return version

        return subprocess.check_output(['/bin/sh', '-c', version])
    finally:
        os.chdir(old_path)


def parse_version(version: str,
                  overriden_settings: Dict[str, str]) -> str:
    return parse_version_with_path(version, os.getcwd(), overriden_settings)
