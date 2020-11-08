# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class material_attribute(models.Model):
#     _name = 'material_attribute.material_attribute'
#     _description = 'material_attribute.material_attribute'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
