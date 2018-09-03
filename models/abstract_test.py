# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Abstract_test(models.AbstractModel):
    _name = 'abstract.test'
    name = fields.Char('Name')
    alt = fields.Char('Alt')
    image = fields.Binary('Image')
    active = fields.Boolean('Active')
    
class Test1(models.Model):
    _name = 'test.test1'
    _inherit = 'abstract.test'

class Test1(models.Model):
    _name = 'test.test2'
    _inherit = 'abstract.test'