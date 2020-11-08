-*- coding: utf-8 -*-

from odoo import models, fields, api


class order_parm(models.Model):
    _name = 'parm.order_parm'
    _description = 'parm.order_parm'

    order_detail_id = fields.Many2one(comodel_name='', string='')
    