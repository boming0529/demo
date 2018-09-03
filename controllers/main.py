# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route(['/test/create'], method="get", website=True, cref=False)
    def get_create(self, **post):
        return request.render('bs_demo.bs_jsignature_test', {'models': None})

    @http.route(['/test/create2'], method="post", website=True, cref=True)
    def post_create(self, **post):
        if post.get('signature'):
            jid = request.env['bs_demo.jsignature'].create({
                'name': post.get('name'),
                'signature': post.get('signature')
            })
            print(jid)
            filename = 'signature_of_%s' %(post.get('name'))
            aid = request.env['ir.attachment'].create({
                'name': post.get('name'),
                'res_model': 'bs_demo.jsignature',
                'res_id': jid.id,
                'type': 'binary',
                'datas_fname': filename,
                'datas': post.get('signature'),
                
            })
            print(aid)
        return request.redirect('/test/create')
