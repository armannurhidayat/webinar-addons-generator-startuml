#!/usr/bin/python
#-*- coding: utf-8 -*-

STATES = [('draft','Draft'), ('open','Open'), ('done','Approved')]
from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class deposit(models.Model):

    _name = "vit.deposit"
    _description = "vit.deposit"
    name = fields.Char( required=True, default="New", readonly=True,  string="Name",  help="")
    amount = fields.Float( string="Amount",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    notes = fields.Text( string="Notes",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    trx_date = fields.Datetime( string="Trx date",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    state = fields.Selection(selection=STATES,  readonly=True, default=STATES[0][0],  string="State",  help="")
    deposit_type = fields.Selection(selection=[('fiat', 'Fiat'), ('coin','Coin')],  string="Deposit type",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    amount_curr = fields.Float( string="Amount curr",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    ref = fields.Text( string="Ref",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    payment_link = fields.Text( string="Payment link",  readonly=True, states={"draft" : [("readonly",False)]},  help="")


    partner_id = fields.Many2one(comodel_name="res.partner",  string="Partner",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    currency_id = fields.Many2one(comodel_name="res.currency",  string="Currency",  readonly=True, states={"draft" : [("readonly",False)]},  help="")

    def action_confirm(self):
        self.state = STATES[1][0]

    def action_done(self):
        self.state = STATES[2][0]

    def action_draft(self):
        self.state = STATES[0][0]

    def unlink(self):
        for me_id in self :
            if me_id.state != STATES[0][0]:
                raise UserError("Cannot delete non draft record!")
        return super(deposit, self).unlink()
