#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class wallet_transaction(models.Model):
    _name = "vit.wallet_transaction"
    _inherit = "vit.wallet_transaction"
