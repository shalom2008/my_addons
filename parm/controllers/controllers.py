# -*- coding: utf-8 -*-
# from odoo import http


# class Parm(http.Controller):
#     @http.route('/parm/parm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/parm/parm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('parm.listing', {
#             'root': '/parm/parm',
#             'objects': http.request.env['parm.parm'].search([]),
#         })

#     @http.route('/parm/parm/objects/<model("parm.parm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('parm.object', {
#             'object': obj
#         })
