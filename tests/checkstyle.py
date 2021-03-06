#!/usr/bin/env python3
"""
Check that PEP8 format is followed

Author: Matthew C. Jones
Email: matt.c.jones.aoe@gmail.com

:copyright: 2020 by Optionset authors, see AUTHORS for more details.
:license: GPLv3, see LICENSE for more details.
"""
import subprocess


def check_format(py_file_path):
    """Check format of Python file. """
    print("="*60)
    run_str = f"pycodestyle -v {py_file_path}"
    subproc = subprocess.run(run_str, shell=True, capture_output=True,
                             check=False)
    print(subproc.stdout.decode('UTF-8'), end='')
    print("="*60)


check_format("../engutils/engutils.py")
check_format("runtests.py")
