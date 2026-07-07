from networking_tool.main import run

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

def test_run_returns_zero():
    assert run(["--version"]) == 0
