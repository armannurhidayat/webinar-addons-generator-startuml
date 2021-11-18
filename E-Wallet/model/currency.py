#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class currency(models.Model):

    _name = "res.currency"
    _description = "res.currency"

    _inherit = "res.currency"
    curr_type = fields.Selection(selection=[('fiat', 'Fiat'), ('coin','Coin')],  string="Curr type",  help="")


