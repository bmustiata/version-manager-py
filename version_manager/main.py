from os import path
import os
import sys
import argparse
import glob

from settings_reader import read_settings_file, Pattern
from options_set import get_parameter_values
from util_find import find

from typing import Callable, Iterable, TypeVar, Union, Dict, List  # NOQA

parser = argparse.ArgumentParser(description='Versions processor')

parser.add_argument('--version', '-v',
                    action='store_true',
                    help='Display the version of a single tracked version.')
parser.add_argument('--all', '-a',
                    action='store_true',
                    help='Display all the tracked versions and their values.')
parser.add_argument('--set', '-s',
                    nargs='+',
                    metavar="NAME=VAL",
                    help='Set values overriding what\'s in the yml files.')

argv = parser.parse_args(sys.argv[1:])

default_settings_file = path.realpath(path.join(os.getcwd(), 'versions.json'))
override_parameters = get_parameter_values(argv.set)
versions_to_process = read_settings_file(default_settings_file, override_parameters)

if argv.version:
    tracked_version = find(lambda it: it.name == argv.version,
                           versions_to_process)

    if not tracked_version:
        print("")
        sys.exit(1)

    print(tracked_version.version)
    sys.exit(0)

if argv.all:
    for it in versions_to_process:
        print("%s => %s" % (it.name, it.version))


files_to_process: Dict[str, List[Pattern]] = dict()
changed_files: bool = False

for tracked_version in versions_to_process:
    for file_name, version_pattern in tracked_version.files.items():
        resolved_names = glob.glob(file_name)

        if not resolved_names:
            print('')
            sys.exit(2)

        for resolved_name in resolved_names:
            file_patterns = files_to_process[resolved_name] or []
            file_patterns.append(version_pattern)
            files_to_process[resolved_name] = file_patterns

for resolved_name, version_patterns in files_to_process.items():
    with open(resolved_name) as resolved_file:
        content = resolved_file.read()
        new_content = content

    print("Patching")

    for version_pattern in version_patterns:
        tracked_version = version_pattern.tracked_version
        print('* ')

        new_content = version_pattern.apply_pattern(new_content)

        if version_pattern.match_count != version_pattern.expected_count:
            print('error')
            sys.exit(3)

    if content == new_content:
        print('same content')
        continue

    changed_files = True

    with open(resolved_name, 'w', encoding='utf-8') as output:
        output.write(new_content)

    print('Updated ')

sys.exit(0 if changed_files else 200)
