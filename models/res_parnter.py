# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResParnter(models.Model):
    _inherit = 'res.partner'

    zipcode = fields.Many2one(
        string='Zip Code',
        comodel_name='areacity',
    )
