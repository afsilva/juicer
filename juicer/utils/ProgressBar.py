# -*- coding: utf-8 -*-
# Juicer - Administer Pulp and Release Carts
# Copyright © 2012, Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from progressbar import Bar, Percentage, ProgressBar
import sys

class ProgessBar(object):
    def __init__(self, maxval):
        widgets = [Bar(), Percentage()]
        self.pbar = progressbar.ProgressBar(widgets=widgets, maxval=maxval).start()

    def update(self, val):
        self.pbar.update(val)

    def finish(self):
        self.pbar.finish()
