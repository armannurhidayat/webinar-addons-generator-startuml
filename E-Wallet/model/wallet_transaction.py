#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class wallet_transaction(models.Model):

    _name = "vit.wallet_transaction"
    _description = "vit.wallet_transaction"
    name = fields.Char( required=True, string="Name",  help="")
    trx_date = fields.Datetime( string="Trx date",  help="")
    amount = fields.Float( string="Amount",  help="")
    notes = fields.Text( string="Notes",  help="")
    trx_type = fields.Selection(selection=[('transfer', 'Transfer'), ('fiat_deposit', 'Fiat Deposit'), ('fiat_withdrawal', 'Fiat Withdrawal'), ('coin_deposit', 'Coin Deposit'), ('coin_withdrawal', 'Coin Withdrawal')],  string="Trx type",  help="")
    amount_curr = fields.Float( string="Amount curr",  help="")


    wallet_id = fields.Many2one(comodel_name="vit.wallet",  string="Wallet",  help="")
    currency_id = fields.Many2one(comodel_name="res.currency",  string="Currency",  help="")
    withdrawal_id = fields.Many2one(comodel_name="vit.withdrawal",  string="Withdrawal",  help="")
    deposit_id = fields.Many2one(comodel_name="vit.deposit",  string="Deposit",  help="")
    transfer_id = fields.Many2one(comodel_name="vit.transfer",  string="Transfer",  help="")
