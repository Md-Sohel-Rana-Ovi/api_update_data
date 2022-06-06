# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Information(models.Model):
    _name = 'information.data'
    _description = 'Update Information'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    roll = fields.Integer(string="Roll")

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
