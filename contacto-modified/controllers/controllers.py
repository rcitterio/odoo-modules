# -*- coding: utf-8 -*-
from odoo import http

# class Contacto-modified(http.Controller):
#     @http.route('/contacto-modified/contacto-modified/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/contacto-modified/contacto-modified/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('contacto-modified.listing', {
#             'root': '/contacto-modified/contacto-modified',
#             'objects': http.request.env['contacto-modified.contacto-modified'].search([]),
#         })

#     @http.route('/contacto-modified/contacto-modified/objects/<model("contacto-modified.contacto-modified"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('contacto-modified.object', {
#             'object': obj
#         })