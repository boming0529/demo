# -*- coding: utf-8 -*-
from odoo.tests import common


class DemoTest(common.TransactionCase):
    def setUp(self):
        super(DemoTest, self).setUp()
        self.jsignature = self.env['bs_demo.jsignature']

    def test_01_some_action(self):
        record = self.jsignature.create({
            'name': 'DemoUnitTest',
        })
        record.some_action()
        self.assertEqual(
            record.name,
            'DemoUnitTest',
            msg="Value changed !")
