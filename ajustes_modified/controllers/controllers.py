# -*- coding: utf-8 -*-
from odoo import http

# class AjustesModified(http.Controller):
#     @http.route('/ajustes_modified/ajustes_modified/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ajustes_modified/ajustes_modified/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ajustes_modified.listing', {
#             'root': '/ajustes_modified/ajustes_modified',
#             'objects': http.request.env['ajustes_modified.ajustes_modified'].search([]),
#         })

#     @http.route('/ajustes_modified/ajustes_modified/objects/<model("ajustes_modified.ajustes_modified"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ajustes_modified.object', {
#             'object': obj
#         })