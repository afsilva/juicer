#!/usr/bin/env python
import unittest
from juicer.juicer.Juicer import Juicer as j
from juicer.juicer.Parser import Parser as pmoney
from juicer.utils import mute
import juicer.common.Cart
import os


class TestJuicer(unittest.TestCase):

    def setUp(self):
        self.parser = pmoney()

        self.cname = 'CHG0DAY'
        self.cpath = os.path.expanduser('~/.juicer-carts/%s.json' % self.cname)

    def test_search(self):
        self.args = self.parser.parser.parse_args('search ruby'.split())
        pulp = j(self.args)
        mute()(pulp.search)(pkg_name=self.args.rpmname)

        self.args = self.parser.parser.parse_args(\
            'search ruby --in qa'.split())
        pulp = j(self.args)
        mute()(pulp.search)(pkg_name=self.args.rpmname)

    def test_workflow(self):
        rpm_path = './share/juicer/empty-0.0.1-1.fc17.x86_64.rpm'

        if os.path.exists(self.cpath):
            os.remove(self.cpath)

        # test uploading an rpm
        self.args = self.parser.parser.parse_args(('upload -r %s %s' % ('hats', rpm_path)).split())
        pulp = j(self.args)
        cart = pulp.create('upload-cart', self.args.r)

        self.args = self.parser.parser.parse_args('push upload-cart'.split())
        pulp = j(self.args)
        mute()(pulp.push)(cart)

        # test creating a cart
        self.args = self.parser.parser.parse_args(('create CHG0DAY -r %s %s' \
                % ('hats', rpm_path)).split())
        pulp = j(self.args)
        mute()(pulp.create)(cart_name=self.args.cartname, cart_description=self.args.r)

        # test pushing a cart
        self.args = self.parser.parser.parse_args(('create %s -r hats %s' \
                % (self.cname, rpm_path)).split())
        pulp = j(self.args)
        cart = juicer.common.Cart.Cart(self.args.cartname, autoload=True, autosync=True)
        mute()(pulp.push)(cart=cart)

        # test promoting a cart
        cart = juicer.common.Cart.Cart(self.cname, autoload=True)
        old_env = cart.current_env

        self.args = self.parser.parser.parse_args(('promote %s' % self.cname).split())
        pulp = j(self.args)
        mute()(pulp.promote)(cart_name=self.args.cartname)

        cart = juicer.common.Cart.Cart(self.cname, autoload=True)

        self.assertFalse(cart.current_env == old_env)

        # test creating a cart from manifest
        new_cname = 'CHG1DAY'

        self.args = self.parser.parser.parse_args(('create %s -f %s' \
                % (new_cname, './share/juicer/rpm-manifest.yaml')).split())
        pulp = j(self.args)
        mute()(pulp.create_manifest)(cart_name=self.args.cartname, manifests=self.args.f)

        cart = juicer.common.Cart.Cart(new_cname, autoload=True)

        self.assertFalse(cart.is_empty())

    def test_show(self):
        self.args = self.parser.parser.parse_args(('show %s' % self.cname).split())
        pulp = j(self.args)
        mute()(pulp.show)(self.cname)

    def test_pull(self):
        if os.path.exists(self.cpath):
            os.remove(self.cpath)

        self.args = self.parser.parser.parse_args(('pull %s' % self.cname).split())
        pulp = j(self.args)
        mute()(pulp.pull)(self.cname)

        self.assertTrue(os.path.exists(self.cpath))

    def test_hello(self):
        self.args = self.parser.parser.parse_args('hello'.split())
        pulp = j(self.args)
        mute()(pulp.hello)()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestJuicer)
    unittest.TextTestRunner(verbosity=2).run(suite)
