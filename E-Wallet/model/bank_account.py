#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class bank_account(models.Model):

    _name = "res.partner.bank"
    _description = "res.partner.bank"

    _inherit = "res.partner.bank"


