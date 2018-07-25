vm 2.0.12
=========

Updates versions across multiple files.

Install
-------

.. code:: sh

    pip install vm

Usage
-----

You need a ``versions.json``, or a ``versions.yml`` where you can
specify for what you're tracking the versions, and what files to be
updated using glob patterns:

.. code:: yaml

    germanium:
      version: 1.10.3
      files:
        README.*: "^(germanium )(.*?)$"
        setup.py: "version='**VERSION**',"
        doc/usage/index.adoc: "^(= Germanium v)(.*?)$"
        germanium/version.py: "current = \"**VERSION**\""

Help:

.. code:: text

    usage: vm [-h] [--display NAME] [--all] [--set NAME=VAL [NAME=VAL ...]]
              [--load FILE] [-t]

    Versions processor

    optional arguments:
      -h, --help            show this help message and exit
      --display NAME, -d NAME
                            Display the version of a single tracked version.
      --all, -a, --list     Display all the tracked versions and their values.
      --set NAME=VAL [NAME=VAL ...], -s NAME=VAL [NAME=VAL ...]
                            Set values overriding what's in the yml files.
      --load FILE, -l FILE  Override versions from the given yml file.
      -t, --tag-name, --tag
                            Get the current name to use in general tags.

Specifying Versions
-------------------

The version value will be expanded using the shell if it contains a '$'
or a '\`', so you can have a version such as:

.. code:: json

    "description": {
      "version": "Build at $(date) on $(uname -n)"
    }

Versions can also refer to other version files, and extract properties
from there, using the ``parent:`` notation in the version:

.. code:: json

    "germaniumdrivers": {
      "version": "parent:../germanium/@germaniumdrivers"
    }

The path will point to the ``versions.json/yml`` file, or to the folder
that contains the ``versions.json/yml`` file, and after that fill will
be read and interpreted the ``germaniumdrivers`` version will be used.

Versions can be also manually overriden from the command line, using the
``--set`` or ``-s`` flag, for example:

.. code:: sh

    vm -s germanium=2.0.8

This will ignore the value specified in the versions.yml file, and use
the specified one.

File Matchers
-------------

There are currently only four file matchers:

RegExp File Matcher
~~~~~~~~~~~~~~~~~~~

It is a RegExp that has two or three groups, and it will have the second
group replaced to the matched version.

**VERSION** File Matcher
~~~~~~~~~~~~~~~~~~~~~~~~

This will construct a RegExp that will match exactly the given text,
with the ``**VERSION**`` being the second group.

So having a matcher such as:

.. code:: json

    "files": {
        "README": "This installs version **VERSION** of the product."
    }

is equivalent with:

.. code:: yaml

    files:
        README: "(This installs version )(.+?)( of the product\\.)"

If the ``**``\ s are replaced with ``^^`` at the beginning, or ``$$`` at
the end, they will act as RegExp anchors, equivalent to ``^`` and ``$``.
In case in the expression there is content before the ``^^``, or after
the ``$$``, the content is ignored.

maven: File Matcher
~~~~~~~~~~~~~~~~~~~

This will construct a RegExp that will match:

.. code:: text

    `(<groupId>${m[1]}</groupId>\\s*` +
    `<artifactId>${m[2]}</artifactId>\\s*` +
    `<version>)(.*?)(</version>)`;

In order to specify the matcher, just use:

.. code:: yaml

    germanium:
      version: 2.0.0
      files:
        pom.xml: maven:com.germaniumhq:germanium

Matcher Constraints
-------------------

In order to make sure that the expressions are not replacing in too many
places, constraints can be added to limit, or extend the matches.

Matcher constraints are always active, and in case no constraint is
specified then the maximum replacement count is set to 1.

Match Count
~~~~~~~~~~~

.. code:: json

    "product" : {
      "version": "1.0",
      "files": {
        "README.md": {
          "match": "^(= Germanium v)(.*?)$",
          "count": 1
        }
      }
    }

The count can be also ``0`` for no matches, or negative to indicate any
number of matches is allowed.

Multiple Matchers
-----------------

In a single file, we can have multiple matchers as well, for example:

.. code:: json

    "product" : {
      "version": "1.0",
      "files": {
        "README.md": [
          "^(= Germanium v)(.*?)$",
          "(Germanium )(\\d+\\.\\d+)()"
        ]
      }
    }

For each matcher that is added, if there is no match count specified,
it's assumed that it will only match once in the file.

Of course, constraints can be applied for both the full set of matchers:

.. code:: json

    "product" : {
      "version": "1.0",
      "files": {
        "README.md": {
          "match": [
            "^(= Germanium v)(.*?)$",
            "(Germanium )(\\d+\\.\\d+)()"
          ],
          "count": 3
        }
      }
    }

or even individual expressions:

.. code:: json

    "product" : {
      "version": "1.0",
      "files": {
        "README.md": {
          "match": [
            "^(= Germanium v)(.*?)$",
            {
              "match": "(Germanium )(\\d+\\.\\d+)()",
              "count": 2
            }
          ],
          "count": 3
        }
      }
    }

Notes
-----

1. Files are actually ``glob`` patterns, so you can match ``**/*.js``
   for example.
2. The configuration files can be yml.
3. ``vm`` will output the following error codes: 0 when no files are
   changed, 0 when files are changed successfuly, or a non zero error
   code in case of error.
