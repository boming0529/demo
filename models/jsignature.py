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
    
    test = fields.Char('test')
