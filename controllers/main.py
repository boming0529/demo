# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route(['/test/create'], type="http", method=["Get"], website=True, cref=False)
    def get_create(self, **post):
        return request.render('bs_demo.bs_jsignature_test', {})

    @http.route(['/test/insert'], type="http", method=["Post"], website=True, cref=True)
    def post_create(self, **post):
        if post.get('signature'):
            jid = request.env['bs_demo.jsignature'].create({
                'name': post.get('name'),
                'signature': post.get('signature')
            })
            filename = 'signature_of_%s' %(post.get('name'))
            aid = request.env['ir.attachment'].create({
                'name': post.get('name'),
                'res_model': 'bs_demo.jsignature',
                'res_id': jid.id,
                'type': 'binary',
                'datas_fname': filename,
                'datas': post.get('signature'),
            })
            jid.write({'signature_id': aid.id})
        return request.render('bs_demo.bs_jsignature_test2', {'member': jid})
