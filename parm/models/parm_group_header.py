-*- coding: utf-8 -*-

from odoo import models, fields, api


class parm_group_header(models.Model):
    _name = 'parm.parm_group_header'
    _description = 'parm.parm_group_header'

    name = fields.Char(string='name')
    parm_id = fields.Many2one(comodel_name='parm.parm', string='')
    is_active = fields.Boolean(string='is_active')
    