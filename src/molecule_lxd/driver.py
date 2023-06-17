#  Copyright (c) 2015-2018 Cisco Systems, Inc.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
import os
from typing import Dict
from molecule import logger
from molecule.api import Driver

LOG = logger.get_logger(__name__)


class LXD(Driver):
    """LXD molecule driver plugin."""

    def __init__(self, config=None):
        super(LXD, self).__init__(config)
        self._name = "lxd"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def login_cmd_template(self):
        return "lxc exec {instance} bash"

    @property
    def default_safe_files(self):
        return []

    @property
    def default_ssh_connection_options(self):
        return []

    def login_options(self, instance_name):
        return {"instance": instance_name}

    def ansible_connection_options(self, instance_name):
        return {
            "ansible_connection": "community.general.lxd",
            "ansible_lxd_remote": os.getenv("LXC_REMOTE", "local"),
        }

    def sanity_checks(self):
        # TODO: Implement sanity checks
        pass

    def template_dir(self):
        return os.path.join(os.path.dirname(__file__), "cookiecutter")

    def modules_dir(self):
        return os.path.join(os.path.dirname(__file__), "modules")

    @property
    def required_collections(self) -> Dict[str, str]:
        return {"community.general": "4.1.0"}
