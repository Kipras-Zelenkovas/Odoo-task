# -*- coding: utf-8 -*-
# from odoo import http


# class Docs(http.Controller):
#     @http.route('/docs/docs/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/docs/docs/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('docs.listing', {
#             'root': '/docs/docs',
#             'objects': http.request.env['docs.docs'].search([]),
#         })

#     @http.route('/docs/docs/objects/<model("docs.docs"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('docs.object', {
#             'object': obj
#         })
