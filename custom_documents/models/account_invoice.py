# © 2018 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class StockIncoterms(models.Model):
    _inherit = "stock.incoterms"

    @api.multi
    def name_get(self):
        return [(record.id, "(%s) %s" % (record.code, record.name)) for record in self]


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    #Deposito / anticipo
    advance = fields.Float(string="Advance")
    balance_outstanding = fields.Float(compute = '_calculate_balance_outstanding', string="Balance outstanding")

    incoterm = fields.Many2one(
        'stock.incoterms', 'Shipment Terms',
        help="International Commercial Terms are a series of predefined commercial terms used in international transactions.")

    port_destination=fields.Text(string= "Port destination")
    unit_type_id = fields.Many2one('sale.order.unit.type', 'Unit types')


    @api.depends('advance','balance_outstanding')
    def _calculate_balance_outstanding(self):
        self.balance_outstanding=self.amount_untaxed - self.advance
