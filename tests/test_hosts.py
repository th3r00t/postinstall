# from typing import assert_type

# import pytest
from pathlib import Path
from ..src.lib.resources import UserData
from ..src.lib.environment import Hosts
ud = UserData()

def test_Hosts():
    hosts = Hosts(ud)
    if hosts.entries:
        assert len(hosts.entries) > 0
        hosts.write_hosts(Path("./hosts"))
        assert Path("./hosts").is_file()
