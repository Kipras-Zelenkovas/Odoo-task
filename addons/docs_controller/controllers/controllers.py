# -*- coding: utf-8 -*-
# from odoo import http


# class DocsController(http.Controller):
#     @http.route('/docs_controller/docs_controller/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/docs_controller/docs_controller/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('docs_controller.listing', {
#             'root': '/docs_controller/docs_controller',
#             'objects': http.request.env['docs_controller.docs_controller'].search([]),
#         })

#     @http.route('/docs_controller/docs_controller/objects/<model("docs_controller.docs_controller"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('docs_controller.object', {
#             'object': obj
#         })
