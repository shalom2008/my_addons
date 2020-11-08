# -*- coding: utf-8 -*-
# from odoo import http


# class UnitGroup(http.Controller):
#     @http.route('/unit_group/unit_group/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unit_group/unit_group/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unit_group.listing', {
#             'root': '/unit_group/unit_group',
#             'objects': http.request.env['unit_group.unit_group'].search([]),
#         })

#     @http.route('/unit_group/unit_group/objects/<model("unit_group.unit_group"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unit_group.object', {
#             'object': obj
#         })
