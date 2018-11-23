# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Jsignature(models.Model):

    _name = 'bs_demo.jsignature'
    name = fields.Char('Name')
    signature = fields.Binary(
        string='Signature',
        store=False,
    )
    signature_id = fields.Many2one(
        string='attachment id of signature',
        comodel_name='ir.attachment',
    )
    test_file = fields.Binary(
        string='Test File',
    )

    test = fields.Char('test')

    @api.multi
    def some_action(self):
        self.name = 'change' + self.name