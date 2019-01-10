# © 2018 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _

class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    booking = fields.Char(string='Booking')
    harbour_id = fields.Many2one('seistag.harbour', string='Harbour')
