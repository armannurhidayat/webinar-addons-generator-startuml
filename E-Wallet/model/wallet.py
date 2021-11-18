#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class wallet(models.Model):

    _name = "vit.wallet"
    _description = "vit.wallet"
    name = fields.Char( required=True, string="Name",  help="")
    balance = fields.Float( string="Balance",  help="")
    wallet_type = fields.Selection(selection=[('fiat', 'Fiat'), ('coin','Coin')],  string="Wallet type",  help="")
    deposit_address = fields.Char( string="Deposit address",  help="")
    balance_network = fields.Float( string="Balance network",  help="")


    partner_id = fields.Many2one(comodel_name="res.partner",  string="Partner",  help="")
    currency_id = fields.Many2one(comodel_name="res.currency",  string="Currency",  help="")
    wallet_transaction_ids = fields.One2many(comodel_name="vit.wallet_transaction",  inverse_name="wallet_id",  string="Wallet transactions",  help="")
