#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class partner(models.Model):

    _name = "res.partner"
    _description = "res.partner"

    _inherit = "res.partner"
    balance = fields.Float( string="Balance",  help="")
    account_number = fields.Char( string="Account number",  help="")


    bank_account_id = fields.Many2one(comodel_name="res.partner.bank",  string="Bank account",  help="ini documentation")
    deposit_ids = fields.One2many(comodel_name="vit.deposit",  inverse_name="partner_id",  string="Deposits",  help="")
    wallet_ids = fields.One2many(comodel_name="vit.wallet",  inverse_name="partner_id",  string="Wallets",  help="")
    transfer_ids = fields.One2many(comodel_name="vit.transfer",  inverse_name="partner_id",  string="Transfers",  help="")
    withdrawal_ids = fields.One2many(comodel_name="vit.withdrawal",  inverse_name="partner_id",  string="Withdrawals",  help="")
