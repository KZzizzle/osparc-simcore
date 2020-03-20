# pylint:disable=unused-variable
# pylint:disable=unused-argument
# pylint:disable=redefined-outer-name

import os
import re
import subprocess
from pathlib import Path

import pytest


@pytest.fixture
def pylintrc(osparc_simcore_root_dir):
    pylintrc_path = osparc_simcore_root_dir / ".pylintrc"
    assert pylintrc_path.exists()
    return pylintrc_path


def test_run_pylint(pylintrc, package_dir):
    cmd = "pylint --jobs 0 --rcfile {} -v {}".format(pylintrc, package_dir)
    assert subprocess.check_call(cmd.split()) == 0


def test_no_pdbs_in_place(package_dir):
    MATCH = re.compile(r"pdb.set_trace()")
    EXCLUDE = ["__pycache__", ".git"]
    for root, dirs, files in os.walk(package_dir):
        for name in files:
            if name.endswith(".py"):
                pypth = Path(root) / name
                code = pypth.read_text()
                found = MATCH.findall(code)
                assert not found, "pbd.set_trace found in %s" % pypth
        dirs[:] = [d for d in dirs if d not in EXCLUDE]
