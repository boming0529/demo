# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class fask_Jsignature(object):
    def __init__(self, **post):
        self.__dict__.update(post)


class Main(http.Controller):
    @http.route(['/test/create'], type="http", auth='public', method=["Get","Post"], website=True)
    def get_create(self, **post):
        return request.render('bs_demo.bs_jsignature_test', {})

    @http.route(['/test/insert'], type="http", auth='public', method=["Post"], website=True, csrf=True)
    def post_create(self, **post):
        jid = None
        error = {}
        if post.get('name') == 'noob':
            error['name'] = 'you shoud been a noob'
            post['name'] = ''
        if not post.get('test'):
            error['test'] = 'the test field is required.'
            post['test'] = ''
        if error: 
            return request.render('bs_demo.bs_jsignature_test', {
                'member': fask_Jsignature(**post),
                'error': error
            })
        if post.get('signature'):
            jid = request.env['bs_demo.jsignature'].sudo().create({
                'name': post.get('name'),
                'signature': post.get('signature')
            })
            filename = 'signature_of_%s' % (post.get('name'))
            aid = request.env['ir.attachment'].sudo().create({
                'name': post.get('name'),
                'res_model': 'bs_demo.jsignature',
                'res_id': jid.id,
                'type': 'binary',
                'datas_fname': filename,
                'datas': post.get('signature'),
            })
            jid.write({'signature_id': aid.id})
        else:
            jid = request.env['bs_demo.jsignature'].sudo().create({
                'name': post.get('name'),
                'signature_id': False,
            })
            jid['test'] = 'test update data after create.'
        return request.render('bs_demo.bs_jsignature_test2', {'member': jid})
