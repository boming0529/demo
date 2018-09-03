# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Jsignature(models.Model):

    _name = 'bs_demo.jsignature'
    name = fields.Char('Name')
    signature = fields.Binary(
        string='Signature',
    )
    
