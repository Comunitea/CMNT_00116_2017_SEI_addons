# © 2019 Comunitea
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    date_order_date = fields.Date(compute='_compute_date_order_date',
                                  store=True)

    @api.depends('date_order')
    def _compute_date_order_date(self):
        for order in self:
            order.date_order_date = fields.Datetime.from_string(
                order.date_order).date()
