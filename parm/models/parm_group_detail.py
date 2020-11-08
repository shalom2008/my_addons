-*- coding: utf-8 -*-

from odoo import models, fields, api


class parm_group_detail(models.Model):
    _name = 'parm.parm_group_detail'
    _description = 'parm.parm_group_detail'

    parm_id = fields.Many2one(comodel_name='parm.parm', string='')
    input_type = fields.Selection([('input','input'),('combol','combol'),('selection','selection')]) 
    # combol可能拼错了 combol,selection都要关联选项，只是录入形式不一样。要看odoo有没有combol
    relat_item =     # 关联item_module里的item
    parm_group_id = fields.Many2one(comodel_name='', string='')
