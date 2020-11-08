# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class unit_group(models.Model):
#     _name = 'unit_group.unit_group'
#     _description = 'unit_group.unit_group'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
