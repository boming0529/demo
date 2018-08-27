# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResParnter(models.Model):
    _inherit = 'res.partner'

    zipcode = fields.Many2one(
        string='Zip Code',
        comodel_name='cityarea',
    )

    @api.onchange('state_id')
    def _onchange_state_id(self):
        res = {'domain': {'zipcode': []}}
        if self.state_id:
            res = {'domain': {'zipcode': [('state_id', '=', self.state_id.id)]}}
        return res
