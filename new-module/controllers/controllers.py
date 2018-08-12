# -*- coding: utf-8 -*-
from odoo import http

# class New-module(http.Controller):
#     @http.route('/new-module/new-module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new-module/new-module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('new-module.listing', {
#             'root': '/new-module/new-module',
#             'objects': http.request.env['new-module.new-module'].search([]),
#         })

#     @http.route('/new-module/new-module/objects/<model("new-module.new-module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new-module.object', {
#             'object': obj
#         })