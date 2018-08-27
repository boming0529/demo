# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AreaCity(models.Model):
    _name = 'cityarea'

    name = fields.Char(
        string='Area',
    )
    
    code = fields.Integer(
        string='zip',
    )

    state_id = fields.Many2one("res.country.state", string='State')
