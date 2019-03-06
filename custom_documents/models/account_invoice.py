# © 2018 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class AccountInvoice(models.Model):
    _inherit = "account.invoice"


    incoterm = fields.Many2one(
        'stock.incoterms', 'Shipment Terms',
        help="International Commercial Terms are a series of predefined commercial terms used in international transactions.")
    port_destination=fields.Text(string= "Port destination")
    unit_type_id = fields.Many2one('sale.order.unit.type', 'Unit types')
