#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class currency(models.Model):
    _name = "res.currency"
    _inherit = "res.currency"
