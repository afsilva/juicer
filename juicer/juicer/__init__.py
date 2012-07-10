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

import juicer.utils.Log
from juicer.juicer.Juicer import Juicer as j
from pprint import pprint as pp


def create(args):
    pulp = j(args)
    juicer.utils.Log.log_info("Creating cart '%s'." % args.cartname)
    cart = pulp.create(args.cartname, args.r)
    juicer.utils.Log.log_info("Saved cart '%s'." % args.cartname)
    print cart


def edit():
    pass


def show(args):
    pulp = j(args)
    cart = pulp.show(args.cartname)
    print cart


def update():
    pass


def createlike():
    pass


def publish():
    pass


def cartsearch(args):
    pass


def rpmsearch(args):
    pulp = j(args)
    pp(pulp.search_rpm(name=args.rpmname, envs=args.environment))


def upload(args):
    pulp = j(args)
    pp(pulp.upload(items=args.item))


def hello(args):
    pulp = j(args)
    pp(pulp.hello(envs=args.environment))
