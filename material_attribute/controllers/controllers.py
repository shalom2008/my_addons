# -*- coding: utf-8 -*-
# from odoo import http


# class MaterialAttribute(http.Controller):
#     @http.route('/material_attribute/material_attribute/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/material_attribute/material_attribute/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('material_attribute.listing', {
#             'root': '/material_attribute/material_attribute',
#             'objects': http.request.env['material_attribute.material_attribute'].search([]),
#         })

#     @http.route('/material_attribute/material_attribute/objects/<model("material_attribute.material_attribute"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('material_attribute.object', {
#             'object': obj
#         })
