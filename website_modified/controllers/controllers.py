# -*- coding: utf-8 -*-
from odoo import http

# class WebsiteModified(http.Controller):
#     @http.route('/website_modified/website_modified/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_modified/website_modified/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_modified.listing', {
#             'root': '/website_modified/website_modified',
#             'objects': http.request.env['website_modified.website_modified'].search([]),
#         })

#     @http.route('/website_modified/website_modified/objects/<model("website_modified.website_modified"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_modified.object', {
#             'object': obj
#         })