###############################################################
# pytest -v --capture=no tests/test_storage_awsobjectstore.py
# pytest -v  tests/test_storage_awsobjectstore.py
# pytest -v --capture=no tests/test_storage_awsobjectstore.py:TestObjectstore.<METHIDNAME>
###############################################################
import os
from pathlib import Path
from pprint import pprint

import pytest
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.util import HEADING
from cloudmesh.common.util import banner
from cloudmesh.common.util import path_expand
from cloudmesh.common.util import readfile
from cloudmesh.common.util import writefile
from cloudmesh.common.variables import Variables
from cloudmesh.storage.Provider import Provider


#
# cms set storage=objstore
#
@pytest.mark.incremental
class TestObjectstorage(object):

    def setup(self):
        variables = Variables()
        self.service = Parameter.expand(variables['storage'])[0]
        self.p = Provider(service=self.service)
        self.sourcedir = path_expand("~/.cloudmesh/storage/test")
        print()


    def test_list(self):
        HEADING()
        StopWatch.start("LIST Directory")
        contents = self.p.list(self.p.service, "/")
        StopWatch.stop("LIST Directory")
        for c in contents:
            pprint(c)

        assert len(contents) > 0
        found = False
        for entry in contents:
            if entry["cm"]["name"] == "a1.txt":
                found = True
        assert found


    def test_results(self):
        HEADING()
        # storage = self.p.service
        service = self.service
        banner(f"Benchmark results for {service} Storage")
        StopWatch.benchmark()
