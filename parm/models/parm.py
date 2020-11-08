-*- coding: utf-8 -*-

from odoo import models, fields, api


class parm(models.Model):
    _name = 'parm.parm'
    _description = 'parm.parm'

    name = fields.Char(required=True)
    symbol = fields.Char(required=True)
    typ = fields.Selection([('int','int'),('char','char')],required=True)
    is_active = fields.Boolean(required=True, default=True)
    is_base = fields.Bool(required=True)
