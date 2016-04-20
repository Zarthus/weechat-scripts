# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Jos Ahrens <zarthus@lovebytes.me>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# ---
#
# Allow use of switching buffers with the command '/<number>', 
# such as '/1', '/15', etc.
#
# Inspired by quickwin.pl for irssi (by mr_flea, @mrflea on GitHub)
#
# This script requires WeeChat versions >= 0.3.4
#
# Script options: none
#
# History:
#  version 1.0 - 2016-04-20
#    Script creation

try:
    import weechat as w
    import_ok = True
except ImportError:
    print("This script must be run under WeeChat")
    print("Get WeeChat now at: https://weechat.org/")
    import_ok = False


import re


SCRIPT_NAME = "quickbuffer"
SCRIPT_AUTHOR = "Zarthus <zarthus@lovebytes.me>"
SCRIPT_VERSION = "1.0"
SCRIPT_LICENSE = "MIT"
SCRIPT_DESC = "Switch buffers using the command \"/<number>\""


QUICKBUFFER_REGEXP = re.compile(r"^/(\d+)\s*$")


def cmd_quickbuffer(data, buffer, command):
    """Any command being run will be checked to see if it matches /<number>, and intercepted if it does"""

    match = QUICKBUFFER_REGEXP.match(command)

    if match:
        w.command(buffer, "/buffer {}".format(match.group(1)))
        return w.WEECHAT_RC_OK_EAT

    return w.WEECHAT_RC_OK


if import_ok and w.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, "", ""):
    w.hook_command_run(
        "1100|*",  # the priority is set above the default (1000) because of WEECHAT_RC_OK_EAT
        "cmd_quickbuffer",
        ""
    )
